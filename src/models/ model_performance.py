import pandas as pd

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

# Select relevant columns for the output
output_df = comparison_df[['School', 'actual_rank', 'predicted_rank', 'rank_difference', 'total_points_actual', 'total_points_predicted', 'total_points_difference', 'average_time_actual', 'average_time_predicted', 'average_time_difference', 'total_time_actual', 'total_time_predicted', 'total_time_difference']]

# Save the model performance assessment to a CSV file
output_file_path = '../../reports/2019_model_performance_assessment.csv'
output_df.to_csv(output_file_path, index=False)

print("Model performance assessment for 2019 is saved.")
