# A Web crawler is an Internet bot which systematically browses the World Wide Web,
# typically for the purpose of Web indexing.

import requests
from bs4 import BeautifulSoup

def irish_castles(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.reddit.com/r/castles/#page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class': 'title may-blank loggedin  srTagged imgScanned'}):
            href = link.get('href')
            print(href)
        page += 1

irish_castles(1)
