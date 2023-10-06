import requests
from bs4 import BeautifulSoup
import pandas as pd
from Extraction import Extraction

# Send an HTTP GET request to the website
url = 'https://www.interviewbit.com/data-science-interview-questions/'

# passing the url to the construct
extract = Extraction(url)

# getting the html content
soup = extract.soup()

question_answer_elements = soup.find_all('div', id='freshers')
question_answer_elements.append(soup.find_all('div', id='experienced')[0])
question_answer_elements.append(soup.find_all('div', id='faqs')[0])

interview_data = []


for qa in question_answer_elements:

    # Find all sections with the specified class
    sections = qa.find_all('section', class_='ibpage-article-header')

    for section in sections:
        # Extract the question
        question_element = section.find('h3')
        question = question_element.text.strip()

        # Extract the answers
        
        answers = []

        answer_elements = section.find_all('article')
        for answer_element in answer_elements:
            answer = answer_element.text.strip()
            answers.append(answer)

        result = " ".join(answers)

        interview_data.append([question, result])

# Create a DataFrame from the list of data
df = pd.DataFrame(interview_data, columns=['Question', 'Answer'])

# Specify the CSV file path
csv_file = "assets/interview_data_interviewbit.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f'Data saved to {csv_file}')






'''
ids = freshers
ids = experienced
ids = faqs
'''

