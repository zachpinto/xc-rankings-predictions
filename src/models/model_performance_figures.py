import pandas as pd
import matplotlib.pyplot as plt

# Load the actual and predicted results for 2019
actual_file_path = '../../reports/2019_team_actual.csv'
predicted_file_path = '../../reports/2019_team_prediction.csv'

actual_df = pd.read_csv(actual_file_path)
predicted_df = pd.read_csv(predicted_file_path)

# Rank the schools by total points in ascending order
actual_df['actual_rank'] = actual_df['total_points'].rank(method='min')
predicted_df['predicted_rank'] = predicted_df['total_points'].rank(method='min')

# Merge the actual and predicted dataframes on the School column
comparison_df = actual_df.merge(predicted_df, on='School', suffixes=('_actual', '_predicted'))

# Calculate the differences between actual and predicted results
comparison_df['rank_difference'] = comparison_df['actual_rank'] - comparison_df['predicted_rank']
comparison_df['total_points_difference'] = comparison_df['total_points_actual'] - comparison_df['total_points_predicted']
comparison_df['average_time_difference'] = comparison_df['average_time_actual'] - comparison_df['average_time_predicted']
comparison_df['total_time_difference'] = comparison_df['total_time_actual'] - comparison_df['total_time_predicted']

# Plot Actual vs. Predicted Ranks
plt.figure(figsize=(10, 6))
plt.scatter(comparison_df['actual_rank'], comparison_df['predicted_rank'])
plt.plot([1, 55], [1, 55], color='red', linestyle='--')  # Diagonal line for perfect prediction
plt.xlabel('Actual Rank')
plt.ylabel('Predicted Rank')
plt.title('Actual vs. Predicted Ranks')
plt.savefig('../../reports/figures/2019_actual_vs_predicted_ranks.png')
plt.close()

# Plot Total Points Difference
plt.figure(figsize=(10, 6))
comparison_df.sort_values('total_points_difference', inplace=True)
plt.bar(comparison_df['School'], comparison_df['total_points_difference'])
plt.xlabel('School')
plt.ylabel('Total Points Difference')
plt.title('Total Points Difference (Actual - Predicted)')
plt.xticks(rotation=90)
plt.savefig('../../reports/figures/2019_total_points_difference.png')
plt.close()

# Plot Average Time Difference
plt.figure(figsize=(10, 6))
comparison_df.sort_values('average_time_difference', inplace=True)
plt.bar(comparison_df['School'], comparison_df['average_time_difference'])
plt.xlabel('School')
plt.ylabel('Average Time Difference (Actual - Predicted)')
plt.title('Average Time Difference (Actual - Predicted)')
plt.xticks(rotation=90)
plt.savefig('../../reports/figures/2019_average_time_difference.png')
plt.close()

# Plot Total Time Difference
plt.figure(figsize=(10, 6))
comparison_df.sort_values('total_time_difference', inplace=True)
plt.bar(comparison_df['School'], comparison_df['total_time_difference'])
plt.xlabel('School')
plt.ylabel('Total Time Difference (Actual - Predicted)')
plt.title('Total Time Difference (Actual - Predicted)')
plt.xticks(rotation=90)
plt.savefig('../../reports/figures/2019_total_time_difference.png')
plt.close()

print("Figures for model performance assessment are saved.")
