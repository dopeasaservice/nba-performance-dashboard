import boto3
import json
import time
from datetime import datetime
from botocore.exceptions import ClientError

def save_to_secrets_manager(bucket_name):
    """Save bucket name to AWS Secrets Manager"""
    secrets_client = boto3.client('secretsmanager')
    secret_name = 'nba_dashboard_secrets'
    
    try:
        # Try to get existing secret
        try:
            response = secrets_client.get_secret_value(SecretId=secret_name)
            existing_secrets = json.loads(response['SecretString'])
        except secrets_client.exceptions.ResourceNotFoundException:
            existing_secrets = {}
        
        # Update secrets with new bucket name
        existing_secrets['RAW_BUCKET_NAME'] = bucket_name
        
        # Create or update secret
        try:
            secrets_client.update_secret(
                SecretId=secret_name,
                SecretString=json.dumps(existing_secrets)
            )
        except secrets_client.exceptions.ResourceNotFoundException:
            secrets_client.create_secret(
                Name=secret_name,
                SecretString=json.dumps(existing_secrets)
            )
            
        print(f"✅ Saved bucket name to Secrets Manager: {secret_name}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to save to Secrets Manager: {str(e)}")
        raise

def create_manifest(bucket_name):
    """Create QuickSight manifest file"""
    try:
        manifest = {
            "fileLocations": [
                {
                    "URIs": [
                        f"s3://{bucket_name}/standings.json",
                        f"s3://{bucket_name}/player_stats.json",
                        f"s3://{bucket_name}/team_stats.json"
                    ]
                }
            ],
            "globalUploadSettings": {
                "format": "JSON",
                "delimiter": ",",
                "containsHeader": True
            }
        }
        
        # Create config directory if it doesn't exist
        import os
        os.makedirs('config', exist_ok=True)
        
        # Write manifest to file
        with open('config/manifest.json', 'w') as f:
            json.dump(manifest, f, indent=4)
            
        print("✅ Created manifest file successfully")
        print("\n📝 Manifest Configuration:")
        print(f"  Bucket: {bucket_name}")
        print("  Files configured:")
        print("   - standings.json")
        print("   - player_stats.json")
        print("   - team_stats.json")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to create manifest: {str(e)}")
        raise

def create_and_configure_bucket():
    """Creates S3 bucket, saves name to Secrets Manager, and creates manifest"""
    s3 = boto3.client('s3')
    region = boto3.session.Session().region_name
    timestamp = datetime.now().strftime('%Y%m%d-%H%M')
    
    # Define bucket name
    bucket_name = f"nba-raw-data-{timestamp}"
    
    print(f"🚀 Starting setup process...")
    print(f"Creating bucket in {region}...")
    
    try:
        # Create bucket with appropriate configuration
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        
        # Enable versioning
        s3.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )
        
        # Add lifecycle rule
        s3.put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration={
                'Rules': [{
                    'Status': 'Enabled',
                    'Expiration': {'Days': 1},
                    'ID': 'DeleteAfter24Hours'
                }]
            }
        )
        
        print(f"✅ Created bucket: {bucket_name}")
        
        # Save bucket name to Secrets Manager
        save_to_secrets_manager(bucket_name)
        
        # Create manifest file
        create_manifest(bucket_name)
        
        print("\n🎉 Setup Complete!")
        print("\n📝 Configuration Summary:")
        print(f"  Bucket Name: {bucket_name}")
        print(f"  Region: {region}")
        print(f"  Versioning: Enabled")
        print(f"  Lifecycle: 24-hour expiration")
        print(f"  Secrets Manager: Updated")
        print(f"  Manifest: Created in config/manifest.json")
        
        return bucket_name
            
    except Exception as e:
        print(f"\n❌ Setup failed: {str(e)}")
        # Cleanup bucket if it was created
        try:
            print(f"🧹 Cleaning up bucket: {bucket_name}")
            s3.delete_bucket(Bucket=bucket_name)
        except Exception as cleanup_error:
            print(f"⚠️  Cleanup error: {str(cleanup_error)}")
        raise

if __name__ == "__main__":
    try:
        bucket_name = create_and_configure_bucket()
        print("\n✨ Setup completed successfully!")
    except Exception:
        print("\n❌ Setup failed - see errors above")
