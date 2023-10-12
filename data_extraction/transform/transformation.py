import pandas as pd
import re
from helpers import *

# read the dataset
df = pd.read_csv('assets/result.csv', index_col=[0])

# Apply the remove_enumeration function to the 'Question' column
df['Question'] = df['Question'].apply(remove_enumeration)

# Preprocess text data (e.g., convert to lowercase)
df['Question'] = df['Question'].str.lower()

indices_to_drop = []

# Iterate through the dataset to find duplicates
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        if are_questions_duplicates(df.at[i, 'Question'], df.at[j, 'Question']):
            print(f"the index now is {j}")
            indices_to_drop.append(j)  # Store the index of the duplicate question

# Drop the duplicate questions from the DataFrame
df_cleaned = df.drop(indices_to_drop)

# Reset the index to ensure it's sequential
df_cleaned.reset_index(drop=True, inplace=True)

df_cleaned.to_csv('assets/final_result.csv')

