from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

print('###################################################################################')
print('Headlines')
print('---------------')
for article in soup.find_all('article'):
    h = article.a.text
    print(h)

# get all the text value of paragraph element.
print('\n')
print('Summary')
print('---------')
for article in soup.find_all('article'):
    p = article.find('div', class_='entry-content').p.text
    print(p)

print('\n')
print('Youtube Link')
print('------------------------')
for article in soup.find_all('article'):
    vid_id = article.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
    youtube_url = f"https://youtube.com/watch?v={vid_id}"
    print(youtube_url)

print('\n')
print('Date And Time')
print('-----------------')
for article in soup.find_all('article'):
    time = article.find('time', class_='entry-time').text
    print(time)

print('\n')
print('Author')
print('---------------')
for article in soup.find_all('article'):
    author = article.find('span', class_='entry-author-name').text
    print(author)

print('\n')

for article in soup.find_all('article'):
    link = article.find_all('span', class_='entry-categories')
    for each in link:
        each = str(each)
        new = each.split(',')
        for i in new:
            soup = BeautifulSoup(i, 'lxml')
        for span in soup.find_all('a'):
            first = span.text
            # second = span.find('a').text
            print(first)
