import json
import boto3
import requests
from datetime import datetime

def get_secret(secret_name):
    """Retrieve secret from AWS Secrets Manager"""
    session = boto3.session.Session()
    secrets_client = session.client(
        service_name='secretsmanager'
    )
    
    try:
        get_secret_value_response = secrets_client.get_secret_value(
            SecretId=secret_name
        )
    except Exception as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = json.loads(get_secret_value_response['SecretString'])
            return secret
        
def lambda_handler(event, context):
    # Get secrets
    secrets = get_secret('nba_dashboard_secrets')
    NBA_API_KEY = secrets['nba_api_key']
    RAW_BUCKET_NAME = secrets['raw_bucket_name']
    
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # API endpoints
    endpoints = {
        'standings': 'https://api.sportsdata.io/v3/nba/scores/json/Standings/2024',
        'player_stats': 'https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2024',
        'team_stats': 'https://api.sportsdata.io/v3/nba/scores/json/TeamSeasonStats/2024'
    }
    
    # Headers for API requests
    headers = {
        'Ocp-Apim-Subscription-Key': NBA_API_KEY
    }
    
    try:
        # Fetch and store data for each endpoint
        for data_type, url in endpoints.items():
            # Get data from API
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            # Upload to S3
            file_name = f'{data_type}.json'
            s3.put_object(
                Bucket=RAW_BUCKET_NAME,
                Key=file_name,
                Body=json.dumps(data),
                ContentType='application/json'
            )
            
        return {
            'statusCode': 200,
            'body': json.dumps('Data collection successful')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
