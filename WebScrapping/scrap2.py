from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
# grab the all the contents in the first article from the website.
article = soup.find('article')
# to get the result to look better use prettify method()
print(article.prettify())

# next we gonna scrap the headline
# headline = article.h2.a.text
# print(headline)

# next get the paragraph in a div in the given article.
summary = article.find('div', class_='entry-content').p.text
print(summary)


