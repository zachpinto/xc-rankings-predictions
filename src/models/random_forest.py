import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load the trained Random Forest model
model = joblib.load('best_model.pkl')

# Load the training data (for feature names)
train_df = pd.read_csv('../../data/processed/data.csv')
X_train = train_df[['Year', 'Grade', 'Time']]

# Feature Importance
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
feature_names = X_train.columns

plt.figure(figsize=(10, 6))
plt.title("Feature Importance")
plt.bar(range(X_train.shape[1]), importances[indices], align="center")
plt.xticks(range(X_train.shape[1]), feature_names[indices], rotation=90)
plt.xlim([-1, X_train.shape[1]])
plt.tight_layout()
plt.savefig('../../reports/figures/feature_importance_rank.png')
plt.close()

# Visualize a Single Decision Tree (first tree in the forest)
plt.figure(figsize=(20, 10))
plot_tree(model.estimators_[0], feature_names=feature_names, filled=True, rounded=True, max_depth=3)
plt.title("Decision Tree Visualization (Tree 1)")
plt.savefig('../../reports/figures/random_forest.png')
plt.close()

print("Feature importance and random forest visualizations are saved.")
