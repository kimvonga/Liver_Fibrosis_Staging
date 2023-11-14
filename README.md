Liver Fibrosis Staging
==============================

## Purpose: 
Akero Therapeutics, Viking Therapeutics, Novo Nordisk, and a number of other biotech companies are developing novel therapies for treating fatty liver disease but screening for qualifying patients can take up to 2 hours per patient. To expedite the screening process, can results from routine annual examinations be used to accurately pre-screen for patient qualification with more than 90% accuracy?

## Source(s): 
https://www.kaggle.com/datasets/fedesoriano/cirrhosis-prediction-dataset \
The dataset from Kaggle contains 418 patient records with data on fibrosis stage, age, sex, height, weight, and a number of blood tests including cholesterol levels.
Another potential source comes from Synthea, hosted on google cloud. Synthea contains synthetic electronic health records.

## Context: 
Fatty liver disease is marked by liver fibrosis, which is categorized into 4 stages. More advanced stages of fibrosis are associated with greater liver damage, which can be identified using blood tests. Qualification for developing therapies is restricted to more advanced tages of fibrosis. By analyzing a series of blood tests and considering patient information such as age, sex, height, and weight, it should be possible to accurately predict the different stages of liver fibrosis. If an accurate model can be developed, then it can facilitate enrollment for clinical trials and, should a therapy be approved, expand access to care. 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
