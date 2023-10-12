import requests
from bs4 import BeautifulSoup
import pandas as pd

class Extraction:
    def __init__(self, url):
        self.url = url

    def real_simulation(self):
        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        return session
    
    def soup(self):

        session = self.real_simulation()

        response = session.get(self.url).text
        # Parse the HTML content
        soup = BeautifulSoup(response, 'html.parser')

        return soup


