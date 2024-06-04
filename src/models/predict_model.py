import pandas as pd
import numpy as np
import joblib

# Load the best model
best_model = joblib.load('best_model.pkl')

# Load the processed data
file_path = '../../data/processed/data.csv'
df = pd.read_csv(file_path)

# Split data into test sets for 2018 and 2019
test_df = df[df['Year'].isin([2018, 2019])]


# Function to predict performance
def predict_performance(model, test_df, year):
    schools = test_df['School'].unique()
    predictions = []

    for school in schools:
        school_df = test_df[(test_df['School'] == school) & (test_df['Year'] == year)]
        if school_df.empty:
            continue

        X_test = school_df[['Year', 'Grade', 'Time']]
        pred_times = model.predict(X_test)
        school_predictions = {'School': school}
        for i, time in enumerate(sorted(pred_times)[:10]):  # Get the top 10 predicted times
            school_predictions[f'Runner_{i + 1}'] = time
        predictions.append(school_predictions)

    return pd.DataFrame(predictions)


# Predict performance for 2018 and 2019
pred_2018 = predict_performance(best_model, test_df, 2018)
pred_2019 = predict_performance(best_model, test_df, 2019)

# Save predictions
pred_2018.to_csv('../../models/predictions_2018.csv', index=False)
pred_2019.to_csv('../../models/predictions_2019.csv', index=False)

print("Predictions for 2018 and 2019 are saved.")
