import requests
from bs4 import BeautifulSoup
import pandas as pd
from Extraction import Extraction

# Send an HTTP GET request to the website
url = 'https://www.springboard.com/blog/data-science/data-science-interview-questions/'

# passing the url to the construct
extract = Extraction(url)

# getting the html content
soup = extract.soup()

# Find all the <h3> elements containing questions
questions = soup.find_all('h3', class_='wp-block-heading')

# Initialize a list to store the data
interview_data = []

# Loop through the questions and find the corresponding answers
for question in questions:
    question_text = question.get_text(strip=True)  # Get the question text
    next_element = question.find_next('p')  # Find the next <p> element (the answer)
    if next_element:
        answer_text = next_element.get_text(strip=True)  # Get the answer text
        interview_data.append([question_text, answer_text])  # Store in the list

# Create a DataFrame from the list of data
df = pd.DataFrame(interview_data, columns=['Question', 'Answer'])

# Specify the CSV file path
csv_file = "assets/interview_data_springboard.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f'Data saved to {csv_file}')