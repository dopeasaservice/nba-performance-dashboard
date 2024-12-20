# NBA Analytics Dashboard

This project creates a serverless NBA statistics dashboard using data from Sportsdata.io API. The system automatically collects, stores, and visualizes NBA statistics including team standings, player performance, and team metrics using AWS services.


## Dashboard Features

### Team Performance Analysis 🏀
- Team rankings
- Conference grouping
- Win percentage analysis
- Scoring Leaders
- Home Wins tracker

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
#### 1. Create Dataset:
   - Use S3 manifest file
   - Import to SPICE

#### 2. Create Visualizations:
   - Team Standings Table
   - Top Players Bar Chart
   - Team Performance KPIs

#### 3. Configure Refresh Schedule:
   - Set up data refresh interval
   - Configure update triggers

## Prerequisites
AWS Account with appropriate permissions
Sportsdata.io API subscription
AWS CLI configured
Python 3.8+

## Services Used
AWS Lambda
Amazon S3
Amazon QuickSight
AWS Secrets Manager

## Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open Pull Request

## Resources
- [AWS AppFlow Documentation](https://aws.amazon.com/appflow/)
- [AWS Glue DataBrew Documentation](https://aws.amazon.com/glue/features/databrew/)
- [Amazon QuickSight Documentation](https://aws.amazon.com/quicksight/)

## License
This project is licensed under the MIT License - see LICENSE.md for details

## Acknowledgments
- CozyCloudCrew
- NBA Stats API from SportsData.io
- AWS Documentation
- Community Contributors

Remember to CleanUpYourCloud!
