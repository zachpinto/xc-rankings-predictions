import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import joblib  # To save the model

df = pd.read_csv('../../data/processed/data.csv')

# Split data into train and test sets
train_df = df[df['Year'].isin(range(2010, 2018))]
test_df = df[df['Year'].isin([2018, 2019])]


# Train models
def train_models(train_df):
    models = [
        ('Linear Regression', LinearRegression()),
        ('Random Forest', RandomForestRegressor(random_state=42)),
        ('Gradient Boosting', GradientBoostingRegressor(random_state=42))
    ]

    best_model = None
    best_score = float('inf')

    X_train = train_df[['Year', 'Grade', 'Time']]
    y_train = train_df['Time'].shift(-1).dropna()
    X_train = X_train.iloc[:-1]  # Drop the last row to match the target variable length

    for name, model in models:
        model.fit(X_train, y_train)
        predictions = model.predict(X_train)
        score = mean_squared_error(y_train, predictions)
        print(f"{name} MSE: {score}")

        if score < best_score:
            best_score = score
            best_model = model

    return best_model

best_model = train_models(train_df)

joblib.dump(best_model, 'best_model.pkl')
