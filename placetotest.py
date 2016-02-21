import requests
from bs4 import BeautifulSoup

def irish_castles(max_pages):
    page = ['?count=', '26', '?count=25&after=t3_44c2az']
    pages = int(page[1])

    while pages <= max_pages:
        url = 'https://www.reddit.com/r/castles/' + ''.join(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class': 'title may-blank loggedin  srTagged imgScanned'}):
            href = link.get('href')
            print(href)

        for link_two in soup.findAll('a', {'rel': 'nofollow next'}):
            href_next = link_two.get('href')
            url_add = href_next[33:]
            url_add_two = url_add[:7]
            url_add_four = url_add[-1:-21]
            url_add_three = url_add[7:-21]
            max_pages = url_add_three

            page = [url_add_two, url_add_three, url_add_four]


irish_castles(50)
