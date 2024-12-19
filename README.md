# NBA Analytics Dashboard

Interactive NBA statistics dashboard built with AWS no-code/low-code services. View team stats, player performance, and season trends through dynamic visualizations.

## Dashboard Features

### Team Analysis 🏀
- Win/Loss Records
- Points Per Game
- Field Goal Percentage 
- Home vs Away Performance
- Conference/Division Standings

### Player Statistics 👤
- Scoring Leaders
- Performance Metrics
- Player Comparisons
- Career Statistics
- Hot/Cold Streaks

### Season Insights 📊
- Win/Loss Trends
- Playoff Race Tracking
- Statistical Leaders
- Head-to-Head Records

## Architecture

Built entirely with AWS no-code/low-code services:

- **Data Collection**: Amazon AppFlow
  - Automated NBA API data ingestion
  - Scheduled daily refreshes
  - Raw data stored in S3

- **Data Processing**: AWS Glue DataBrew
  - Visual data transformations
  - Calculated metrics
  - Data quality validation

- **Visualization**: Amazon QuickSight
  - Interactive dashboards
  - Drill-down capabilities
  - Auto-refresh enabled

## Project Structure
nba-analytics-dashboard/
├── appflow/
│   └── flows/
│       ├── nba_teams_flow.json        # Teams data collection flow
│       ├── nba_players_flow.json      # Players data collection flow
│       └── nba_games_flow.json        # Games data collection flow
│
├── databrew/
│   └── recipes/
│       ├── teams/
│       │   ├── standings.json         # Team standings transformation
│       │   ├── stats.json            # Team statistics cleanup
│       │   └── rankings.json         # Team rankings calculations
│       ├── players/
│       │   ├── stats.json            # Player statistics cleanup
│       │   ├── averages.json         # Player averages calculation
│       │   └── leaders.json          # League leaders processing
│       └── games/
│           ├── scores.json           # Game scores processing
│           ├── trends.json           # Win/loss trends
│           └── predictions.json      # Game predictions prep
│
├── quicksight/
│   ├── datasets/
│   │   ├── team_performance.json     # Team performance dataset
│   │   ├── player_stats.json        # Player statistics dataset
│   │   └── season_analysis.json     # Season trends dataset
│   │
│   ├── dashboards/
│   │   ├── team_insights/
│   │   │   ├── overview.json        # Team overview dashboard
│   │   │   ├── comparison.json      # Team comparison dashboard
│   │   │   └── trends.json          # Team trends dashboard
│   │   │
│   │   ├── player_insights/
│   │   │   ├── overview.json        # Player overview dashboard
│   │   │   ├── leaders.json         # Statistical leaders dashboard
│   │   │   └── comparison.json      # Player comparison dashboard
│   │   │
│   │   └── season_insights/
│   │       ├── standings.json       # League standings dashboard
│   │       ├── playoff_race.json    # Playoff analysis dashboard
│   │       └── predictions.json     # Season predictions dashboard
│   │
│   └── analysis/
│       ├── calculated_fields.json   # QuickSight calculated fields
│       └── parameters.json         # QuickSight parameters
│
├── docs/
│   ├── setup/
│   │   ├── appflow.md              # AppFlow setup guide
│   │   ├── databrew.md             # DataBrew setup guide
│   │   └── quicksight.md           # QuickSight setup guide
│   │
│   ├── images/
│   │   ├── dashboards/             # Dashboard screenshots
│   │   └── architecture/           # Architecture diagrams
│   │
│   └── maintenance/
│       ├── refresh.md              # Data refresh guide
│       └── troubleshooting.md      # Troubleshooting guide
│
├── .gitignore                      # Git ignore file
├── LICENSE                         # Project license
└── README.md                       # Project documentation




## Setup Guide

### Prerequisites
- AWS Account
- QuickSight Enterprise Edition
- NBA API access

### Quick Start
1. **Data Collection**
   - Configure AppFlow for NBA API connection
   - Set up S3 buckets for data storage
   - Enable daily refresh schedule

2. **Data Processing**
   - Import DataBrew recipes
   - Configure transformation jobs
   - Set up data validation

3. **Dashboard Setup**
   - Create QuickSight datasets
   - Import dashboard templates
   - Configure auto-refresh

Detailed setup instructions available in `/docs/setup/`

## Data Refresh
- NBA data refreshed daily via AppFlow
- Automated DataBrew transformations
- QuickSight dashboards auto-update

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

---
Built with ❤️ using AWS no-code services
