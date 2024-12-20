# NBA Analytics Dashboard Overview

This project creates a serverless NBA statistics dashboard using data from Sportsdata.io API. The system automatically collects, stores, and visualizes NBA statistics including team standings, player performance, and team metrics using AWS services.

## Dashboard Features

### Team Performance Analysis 🏀
- Team rankings
- Conference grouping
- Win percentage analysis
- Scoring Leaders
- Home Wins tracker

----

## Architecture
This architecture is built using only serverless services to take full advantage of the cloud.

Sportsdata.io API → Lambda → S3 → QuickSight → Dashboard

Components:
1. Data Source: Sportsdata.io API
2. API Key Storage: AWS Secrets Manager
3. Data Collection: AWS Lambda
4. Data Storage: Amazon S3
5. Data Processing & Visualization: Amazon QuickSight


## Project Structure
├── lambda/
│   └── nba_data_collector/
│       ├── lambda_function.py    # API data collection logic
│       └── requirements.txt      # Python dependencies
│
├── quicksight/
│   └── manifest.json            # S3 data source configuration
│
├── s3/
│   └── raw/
│       ├── standings/
│       ├── player_stats/
│       └── team_stats/
│
└── README.md


## Prerequisites
AWS Account with appropriate permissions
Sportsdata.io API subscription
AWS CLI configured
Python 3.8+

## Setup Guide

### 1. API Configuration
#### Set up Sportsdata.io API credentials
- Register at Sportsdata.io
- Obtain API key
- Store API key in AWS Secrets Manager

### 2.Lambda Deployment
#### Deploy data collection Lambda function
- Create Lambda function
- Set environment variables
- Configure API trigger
- Set execution role permissions

### 3. S3 Configuration
#### S3 bucket structure
s3://nba-raw-data-{timestamp}/
  ├── raw/
      ├── standings/data.json
      ├── player_stats/data.json
      └── team_stats/data.json

### 4. QuickSight Setup
#### Manifest file configuration
```
{
    "fileLocations": [
        {
            "URIs": [
                "s3://nba-raw-data-20241218023959/raw/standings/data.json",
                "s3://nba-raw-data-20241218023959/raw/player_stats/data.json",
                "s3://nba-raw-data-20241218023959/raw/team_stats/data.json"
            ]
        }
    ],
    "globalUploadSettings": {
        "format": "JSON",
        "delimiter": ",",
        "containsHeader": true
    }
}
```

### 5. Dashboard Configuration
#### A. Create Dataset:
   - Use S3 manifest file
   - Import to SPICE

#### B. Create Visualizations:
   - Team Standings Table
   - Top Players Bar Chart
   - Team Performance KPIs

#### C. Configure Refresh Schedule:
   - Set up data refresh interval
   - Configure update triggers



## Acknowledgments
- CozyCloudCrew
- NBA Stats API from SportsData.io
- AWS Documentation
- Community Contributors

Remember to CleanUpYourCloud!



---
## NBA Analytics Dashboard Resources
### API Data Source [1]
Sportsdata.io NBA API Documentation: https://sportsdata.io/developers/api-documentation/nba

### Lambda
AWS Lambda Developer Guide: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
Python Lambda Functions: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html
Lambda Environment Variables: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html

### S3
S3 User Guide: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
S3 JSON Object Guide: https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html

### QuickSight
QuickSight User Guide: https://docs.aws.amazon.com/quicksight/latest/user/welcome.html
S3 Files in QuickSight: https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-s3.html
Manifest File Reference: https://docs.aws.amazon.com/quicksight/latest/user/supported-manifest-file-format.html

### AWS SDK for Python (Boto3)
Boto3 Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
S3 Boto3 Guide: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

### AWS CLI
AWS CLI Installation: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
AWS CLI Configuration: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

### AWS IAM
IAM User Guide: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
IAM Role Creation: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html

### AWS Secrets Manager
Secrets Manager User Guide: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
Store and Retrieve Secrets: https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html
-------


## Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open Pull Request

## License
This project is licensed under the MIT License - see LICENSE.md for details


