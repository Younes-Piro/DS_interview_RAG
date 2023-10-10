import pandas as pd
import re

def remove_enumeration(text):
    # Use regular expressions to remove enumeration (e.g., "1.", "2.")
    cleaned_text = re.sub(r'^\d+\.\s+', '', text)
    return cleaned_text

df = pd.read_csv('assets/result.csv', index_col=[0])

# Apply the remove_enumeration function to the 'Question' column
df['Question'] = df['Question'].apply(remove_enumeration)

print(df)

