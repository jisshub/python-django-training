from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('article')

# to get the value of src attribute of the video link,
iframe = article.find('iframe', class_='youtube-player')
print(iframe)

# here to get the attribute of an element, enclose that attribute in a square brackets,
# like v access the value of key in a dictionary
src = article.find('iframe', class_='youtube-player')['src']
print(src)
# here src variable will be a str object.


# if v want the value of style attribute of that element.
style = article.find('iframe', class_='youtube-player')['style']
print(style)


