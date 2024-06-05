import pandas as pd
from scipy.stats import spearmanr
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the actual and predicted results for 2019
actual_file_path = '../../reports/2019_team_actual.csv'  # Update this path to the location of your actual results file
predicted_file_path = '../../reports/2019_team_prediction.csv'  # Update this path to the location of your predicted results file

actual_df = pd.read_csv(actual_file_path)
predicted_df = pd.read_csv(predicted_file_path)

# Rank the schools by total points in ascending order
actual_df['actual_rank'] = actual_df['total_points'].rank(method='min')
predicted_df['predicted_rank'] = predicted_df['total_points'].rank(method='min')

# Merge the actual and predicted dataframes on the School column
comparison_df = actual_df.merge(predicted_df, on='School', suffixes=('_actual', '_predicted'))

# Calculate rank correlation
spearman_corr, _ = spearmanr(comparison_df['actual_rank'], comparison_df['predicted_rank'])

# Calculate Mean Absolute Error (MAE) of ranks
mae_ranks = mean_absolute_error(comparison_df['actual_rank'], comparison_df['predicted_rank'])

# Calculate Mean Squared Error (MSE) of ranks
mse_ranks = mean_squared_error(comparison_df['actual_rank'], comparison_df['predicted_rank'])

# Save the rank accuracy metrics to a text file
output_file_path = '../../reports/2019_rank_accuracy_metrics.txt'
with open(output_file_path, 'w') as file:
    file.write(f"Spearman's Rank Correlation: {spearman_corr}\n")
    file.write(f"Mean Absolute Error (MAE) of Ranks: {mae_ranks}\n")
    file.write(f"Mean Squared Error (MSE) of Ranks: {mse_ranks}\n")

print("Rank accuracy metrics for 2019 are saved.")
