import pandas as pd

# Load the predictions
file_path = '../../models/predictions_2019.csv'
pred_df = pd.read_csv(file_path)

# Melt the dataframe to have one row per runner
melted_df = pred_df.melt(id_vars=['School'], var_name='Runner', value_name='Time')

# Rank runners by time in ascending order
melted_df = melted_df.sort_values(by='Time').reset_index(drop=True)

# Initialize a dictionary to track the number of runners per school
runner_count = {school: 0 for school in melted_df['School'].unique()}

# Initialize a list to store points
points = []

# Iterate through the sorted dataframe and assign points
current_points = 1
for index, row in melted_df.iterrows():
    school = row['School']
    if runner_count[school] < 7:
        points.append(current_points)
        current_points += 1
    else:
        points.append(None)
    runner_count[school] += 1

melted_df['Points'] = points

# Select the required columns and save the results
output_df = melted_df[['School', 'Runner', 'Time', 'Points']]
output_file_path = '../../reports/2019_race_prediction.csv'  # Update this path to where you want to save the file
output_df.to_csv(output_file_path, index=False)

print("2019 race predictions with points are saved.")
