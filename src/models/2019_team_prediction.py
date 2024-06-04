import pandas as pd

# Load the race predictions
file_path = '../../reports/2019_race_prediction.csv'  # Update this path to the location of your file
df = pd.read_csv(file_path)

# Filter out runners that do not have points (i.e., runners 8, 9, 10)
df = df.dropna(subset=['Points'])

# Calculate the total points, total time, and average time for each school
team_stats = df.groupby('School').agg(
    total_points=('Points', 'sum'),
    total_time=('Time', 'sum'),
    average_time=('Time', 'mean')
).reset_index()

# Sort the teams by total points in ascending order
team_stats = team_stats.sort_values(by='total_points', ascending=True)

# Save the team statistics to a new CSV file
output_file_path = '../../reports/2019_team_prediction.csv'  # Update this path to where you want to save the file
team_stats.to_csv(output_file_path, index=False)

print("2019 team predictions are saved.")
