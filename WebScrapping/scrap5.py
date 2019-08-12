from bs4 import BeautifulSoup
from csv import writer
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
    p = str(p)
    smry = p.split(',')[1].split('.')[0]
    print(smry)

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
print('Tags')
print('------------------')
for article in soup.find_all('article'):
    link = article.find_all('span', class_='entry-categories')
    for each in link:
        each = str(each)
        new = each.split(',')
    for i in new:
        soup = BeautifulSoup(i, 'lxml')
        # print(soup)
    for span in soup.find_all('a'):
        text = span.text
        print(text)
        # print(span.a.text)
    #         first = span.text
    #         # second = span.find('a').text
    #         print(first)

with open('web_info.csv', 'w') as csv_file:
    write_obj = writer(csv_file)
    write_obj.writerow(['Headlines', 'Summary', 'Youtube URL', 'Date & Time', 'Author', 'Tags'])
    # write_obj.next()
    for each in write_obj:
        write_obj.writerow()
