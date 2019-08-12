from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find_all('div')
for each in article:
    print(each.p.text)
