# Data Visualization

## Layour Arrangement
[KPI 1][KPI 2][KPI 3]
[Top Teams]
[Team Performance]

## 1. Team Standings breakdown:

### Dimensions (categorical data):
Team Name
Conference
Division

### Values (metrics/measures):
Wins (number)
Losses (number)
Win Percentage (calculated field)

## To create in QuickSight:

1. Create Table Visual
2. Add Fields:
   Dimensions (drop in Field Wells under 'Group by'):
   - Team Name
   - Conference
   
   Values (drop in Field Wells under 'Values'):
   - Wins
   - Losses
   - Win Percentage (if not available, create calculated field)

## Calculated field customization (Win Percentage)

1. Click '+ Add' in Field Wells
2. Choose 'Add calculated field'
3. Name: "Win Percentage"
4. Formula: wins / (wins + losses)
5. Format as percentage

### Sort the table:
- Click the 'Win Percentage' column header
- Choose descending order (high to low)

## Top Teams PPG
### Visual Type: Vertical Bar Chart

Fields:
Dimensions (X-axis):
- Player Name

Values (Y-axis):
- Points Per Game

Settings:
- Limit data to top 10 rows
- Sort by Points Per Game (descending)
- Add Team Name as color


## Team Performance KPIs
Create 3 separate KPI visuals:

1. League Average Points KPI:
   - Metric: Average of Points Per Game
   - Display as: Actual value
   - Format: Round to 1 decimal

2. Highest Scoring Team KPI:
   - Metric: Maximum of Points Per Game
   - Show Team Name
   - Format: Round to 1 decimal

3. Most Wins KPI:
   - Metric: Maximum of Wins
   - Show Team Name
   - Format: Whole number


