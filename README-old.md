# NBA Analytics Dashboard

Interactive dashboard for NBA statistics and analysis powered by Amazon Web Services (AWS) & SportsData.io

## Dashboard Components

### Team Analysis
- Team Performance Metrics
  - Win/Loss Records
  - Points Per Game
  - Field Goal Percentage
  - Defensive Rating
- Conference/Division Standings
  - Real-time Rankings
  - Playoff Race Tracking
- Home vs Away Performance
  - Venue-specific Statistics
  - Win Percentage Splits

### Player Statistics
- Scoring Leaders
  - Points Per Game
  - Field Goal Efficiency
  - Three-Point Percentage
- Performance Metrics
  - Player Efficiency Rating (PER)
  - True Shooting Percentage
  - Plus/Minus Statistics
- Player Comparisons
  - Head-to-head Stats
  - Historical Comparisons
  - Career Trajectories

### Season Insights
- Win/Loss Trends
  - Streak Analysis
  - Monthly Performance
  - Strength of Schedule
- Statistical Leaders
  - Individual Categories
  - Team Rankings
  - League Records
- Playoff Race Tracking
  - Magic Numbers
  - Elimination Scenarios
  - Seeding Predictions

## Project Structure
nba-analytics-dashboard/
├── config/
│   ├── parameters/
│   │   ├── parameter-store/
│   │   │   └── params.json    # Non-sensitive parameters
│   │   └── secrets/
│   │        └── secrets.json  # Template for secrets (no actual values)
│
├── data/
│   ├── raw/
│   │   ├── teams/            # Raw team data
│   │   ├── players/          # Raw player statistics
│   │   └── games/            # Raw game data
│   └── processed/
│       ├── teams/            # Processed team analytics
│       ├── players/          # Processed player analytics
│       └── aggregated/       # Combined analytics
│
├── dashboards/
│   ├── team_analysis/
│   │   ├── performance.json  # Team performance dashboard
│   │   ├── comparison.json   # Team comparison dashboard
│   │   └── trends.json       # Team trends dashboard
│   ├── player_stats/
│   │   ├── overview.json     # Player overview dashboard
│   │   ├── leaders.json      # Statistical leaders dashboard
│   │   └── profiles.json     # Individual player profiles
│   └── season_trends/
│       ├── standings.json    # League standings dashboard
│       ├── playoffs.json     # Playoff analysis dashboard
│       └── predictions.json  # Season predictions dashboard
│
├── docs/
│   ├── setup/
│   │   ├── aws-setup.md     # AWS configuration guide
│   │   ├── quicksight.md    # QuickSight setup guide
│   │   └── parameters.md    # Parameter store setup
│   ├── images/
│   │   ├── dashboards/      # Dashboard screenshots
│   │   └── diagrams/        # Architecture diagrams
│   └── api/
│       ├── endpoints.md      # API endpoint documentation
│       └── schemas.md        # Data schemas
│
├── scripts/
│   ├── data_prep/
│   │   ├── clean_data.py    # Data cleaning scripts
│   │   ├── transform.py     # Data transformation
│   │   └── validate.py      # Data validation
│   ├── refresh/
│   │   ├── daily_update.py  # Daily refresh script
│   │   └── sync.py         # Data synchronization
│   └── validation/
│       ├── quality_check.py # Data quality tests
│       └── schema_check.py  # Schema validation
│
├── tests/
│   ├── data_tests/          # Data validation tests
│   ├── script_tests/        # Script unit tests
│   └── integration_tests/   # Integration tests
│
├── .gitignore              # Git ignore file
├── LICENSE                 # Project license
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies




## Tech Stack
- AWS QuickSight (Dashboard Creation)
- Amazon S3 (Data Storage)
- AWS Systems Manager Parameter Store (Configuration Management)
- AWS Glue (Data Preparation)
- Amazon EventBridge (Automation Scheduling)

## Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured locally
- Access to NBA data source/API
- QuickSight Enterprise Edition

## Getting Started
1. Clone the repository

```bash
git clone https://github.com/dopeasaservice/nba-analytics-dashboard.git
cd nba-analytics-dashboard
```

2. Set up AWS resources
```
# Configure AWS credentials
aws configure

# Set up parameters in Parameter Store
aws ssm put-parameter --name "/nba-analytics/environment/dev/buckets/source-bucket" --value "your-bucket-name" --type "String"
```
3. Initialize data storage

```
# Create S3 buckets
aws s3 mb s3://your-raw-data-bucket
aws s3 mb s3://your-processed-data-bucket
```

4. Configure QuickSight
-Set up data source connections
-Import dashboard templates
-Configure refresh schedules

Data Refresh Process
-Automated daily updates via EventBridge
-Data validation checks
-Dashboard refresh triggers

Contributing
-Fork the repository
-Create your feature branch ( git checkout -b feature/AmazingFeature)
-Commit your changes ( git commit -m 'Add some AmazingFeature')
-Push to the branch ( git push origin feature/AmazingFeature)
-Open a Pull Request

License
-This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments
-NBA Stats API from SportsData.io
-CozyCloudCrew
-AWS Documentation
-Community Contributors

Contact
-George "SpenTheCloud" Parker - https://linkedin.com/in/gsp3
-Project Link: https://github.com/your-username/nba-analytics-dashboard
