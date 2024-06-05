# XC Team Ranking Prediction

## Overview
This project aims to predict the team rankings of (my former) high school cross-country league. 
A Random Forest Classifier performed the best with a Spearman's Rank Correlation of 0.91 (indicating that the model was fairly reliable at predicting team ranking when compared to actual rankings).

For more context:
- Cross-country teams send up to 10 runners to compete in the league's championships; however, only the top 5 runners' scores are counted towards the team's total score (with the caveat of ties, in which case the 6th and 7th runners' accrued scores can be counted). In 2019, 55 teams competed, totaling hundreds of runners.
- Scoring methodology is calculated by summing the top 5 runners' placements (1st place = 1 point, 2nd place = 2 points, etc.), with the non-scoring runners being skipped and having the next point increment being alloted to the next (scoring-eligible) runner. The team with the lowest score wins. This does not neccessarily imply the team with the lowest average or lowest total time wins.
- I was curious whether it was possible to predict the following year's league championship rankings based purely on historical league champsionship data. There are two interesting aspects of this project:
  - Since we are not directly predicting the rankings of the teams based on historical team rankings, it is neccessary to predict the individual finishing times of a given school's (scoring-eligible) runners, thus determining the race rankings at the individual level, and _thus_ determining the team rankings. (Which is the end goal)
  - At the individual level, runners cannot compete past grade 12, thus for the target year (2019), many school's will not have clearly defined scoring eliglbe runners. Therefore, the model mitigates this issue by creating "imputed" runners who will have to neccessarily fill the void of the recently graduated runners. This imputation is done by taking a moving average of top finishing runners from the school's past performances.

## Getting Started
### Prerequisites
- Python 3.8+
- Scikit-Learn
- Pandas

### Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/zachpinto/xc-rankings-predictions.git
cd xc-rankings-predictions
pip install -r requirements.txt
```

## Usage

1. **Run the data preprocessing scripts**:
```bash
python src/data/2010.py
python src/data/2011.py
python src/data/2012.py
python src/data/2013.py
python src/data/2014.py
python src/data/2015.py
python src/data/2016.py
python src/data/2017.py
python src/data/2018.py
python src/data/2019.py
```

2. **Preprocessing for merged dataframe**:
```bash
python notebooks/00_preprocessing.ipynb
python notebooks/02_feature.ipynb
```

3. **Train model**:
```bash
python src/models/train_model.py
```

4. **Predict model**:
```bash
python src/models/predict_model.py
```

5. **Evaluate the model performance**:
```bash
python src/models/2019_race_actual.py
python src/models/2019_race_prediction.py
python src/models/2019_team_actual.py
python src/models/2019_team_prediction.py
python src/models/model_accuracy.py
python src/models/model_performance_figures.py
python src/models/random_forest.py
```
   
## Acknowledgments
- section2harrier.com for his meticulous record-keeping of historical section 2 XC & TF data.

## Directory Structure

```plaintext
xc-rankings-predictions/
│
├── data/
│   ├── interim/        # Standarized race data (years 2010-2019) with core features 
│   ├── processed/      # Processed data for modeling
│   └── raw/            # Raw, scraped race data (years 2010-2019) from section2harrier.com
├── docs/               # Documentation files and project notes
├── notebooks/          # Jupyter notebooks for preprocessing, EDA, feature verificaiton
├── references/         # Data dictionaries (mapping school names to IDs)
├── reports/            # Predictions, model assessments, and metrics
│   └── figures/        # Model performance visualizations and figures
├── src/                # Source code for use in this project
│   ├── __init__.py     # Makes src a Python module
│   ├── data/           # Scripts to download or generate data
│   ├── models/         # Scripts to train models and then use trained models to make predictions
├── LICENSE             # The full license description
├── Makefile            # Makefile with commands like `make data` or `make train`
├── README.md           # The top-level README for developers using this project
├── requirements.txt    # The requirements file for reproducing the analysis environment
├── setup.py            # Makes project pip installable (pip install -e .) so src can be imported
├── test_environment.py # Test python environment is set-up correctly
└── tox.ini             # tox file with settings for running tox; see tox.readthedocs.io

