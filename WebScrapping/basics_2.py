from bs4 import BeautifulSoup

with open('data.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# to get the all h2 tags and its text value
print(soup.find_all('h2'))
for each in soup.find_all('h2'):
    print(each.text)
print(soup.find('h2').text)

# here v first find div with class article1 and later find the h2 tag and its text.
article = soup.find('div', class_='article1')
print(article.find('h2').text)
# grab the paragraph of that article.
print(article.find('p').text)










