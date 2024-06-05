# Phishing Website Prediction using Neural Networks and Logistic Regression

This is a CS 180 Project presented by Masayuki Inukai and Arturo Miguel Saquilayan.

## Dataset Used

- final_dataset.csv found in https://drive.google.com/file/d/18lZyHHdRTaXNK_jwWwh9Y9XW2TLp8WcJ/view?usp=drive_link
  Note: dataset was formed by combining training.csv and testing.csv, which originated from this Kaggle dataset (https://www.kaggle.com/datasets/hemanthpingali/phishing-url/data) made by Hemanth Pingali

## Resulting Model
- The model can be found in this link (https://drive.google.com/file/d/1bmdBLZwr9uHlCrHUvrABbiGAnmjkDxzZ/view?usp=drive_link)

## Processed Dataset
- final_dataset_scaled.csv found in https://drive.google.com/file/d/1EtHMBSXZ8Ld6B86GLVlugMlX0JOwMYXa/view?usp=drive_link

## Code Structure

### Data Preprocessing

- Reduce columns that only have one unique value
- Drop `url` column
- Convert `status` column to int (Flagged `phishing` as 1 and `legitimate` as -1)
- Normalize dataset

### Data Modelling

- Randomize the rows
- Split 80% of the dataset for training, while remaining 20% for testing
- Use `MLPClassifier` for neural networks
- Use `LogisticRegression` for logistic regression

### Hyperparameter Tuning using `GridSearchCV`

- Declare parameters
- Use `GridSearchCV` to tune the model

## How to run code
- Download .zip file
- Open terminal
- Go to root folder of .zip file
- Open models folder
- Run detect-phishing-website.py
