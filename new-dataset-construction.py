import pandas as pd

training_set = pd.read_csv('./datasets/training.csv')
testing_set = pd.read_csv('./datasets/testing.csv')

# Concatenating the dataframes into one
final_dataset = pd.concat([training_set, testing_set]).reset_index(drop=True)
print(final_dataset.head())
final_dataset.to_csv('./datasets/new_dataset.csv', index=False)