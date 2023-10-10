import pandas as pd 
import os

folder_path = './assets'

csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

dataframes = []  # List to store DataFrames for each CSV file

for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Assuming you have a list of DataFrames called 'dataframes'
merged_df = pd.concat(dataframes, ignore_index=True)


result_path = "assets/"

merged_df.to_csv(f'{result_path}result.csv')