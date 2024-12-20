# NBA Stats Data Collection Lambda
This component handles NBA statistics data collection from the SportsData.io API and stores it in S3.

## Data Sources
- Team Standings
- Player Season Statistics
- Team Season Statistics

## Setup

### Prerequisites
- AWS Account with appropriate permissions
- SportsData.io NBA API key
- Python 3.9 or later
- AWS CLI configured

### AWS Resources Required
- AWS Secrets Manager
- S3 Bucket
- IAM Roles and Policies

## Initial Configuration

1. Store API key in AWS Secrets Manager:
```bash
aws secretsmanager create-secret \
    --name nba_dashboard_secrets \
    --secret-string '{"nba_api_key":"your_sportsdata_io_api_key"}'
```
2. Run the bucket creation script:
python create_buckets.py

This script will:
- Create a timestamped S3 bucket (format: nba-raw-data-YYYYMMDD-HHMM)
- Store the bucket name in Secrets Manager
- Generate the QuickSight manifest file

## IAM Permissions
Two IAM policies are provided in the iam/ directory:
- bucket_creation_policy.json: For bucket creation script
- lambda_execution_policy.json: For Lambda function execution

## Data Collection Process
### S3 Storage Structure
nba-raw-data-{timestamp}/
├── standings.json
├── player_stats.json
└── team_stats.json

### API Endpoints
endpoints = {
    'standings': 'https://api.sportsdata.io/v3/nba/scores/json/Standings/2024',
    'player_stats': 'https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2024',
    'team_stats': 'https://api.sportsdata.io/v3/nba/scores/json/TeamSeasonStats/2024'
}

## Lambda Function
### Environment Variables
All configuration is stored in AWS Secrets Manager under 'nba_dashboard_secrets':
- NBA_API_KEY
- RAW_BUCKET_NAME

### Deployment
1. Create Lambda function using provided IAM role

2. Deploy code from lambda/data_collector/

3. Set appropriate timeout (recommended: 30 seconds)

4. Configure memory allocation (recommended: 128MB)

### Testing
#### Test event structure:

{
    "test_type": "full_collection"
}

#### Expected Response:
{
    "statusCode": 200,
    "body": {
        "message": "Data collection complete",
        "results": {
            "standings": "success",
            "player_stats": "success",
            "team_stats": "success"
        }
    }
}

### Monitoring
CloudWatch Logs capture all API calls and S3 operations
Each data collection attempt is logged
Success/failure status for each endpoint
S3 storage confirmation

### Data Lifecycle
S3 bucket has versioning enabled
Objects expire after 24 hours
Failed collections are logged and reported

### Error Handling
API request failures
S3 storage issues
Secret retrieval errors
Invalid API responses

### Future Improvements
Add data validation
Implement retry mechanism
Add CloudWatch metrics
Add data quality checks
Implement cross-region replication
