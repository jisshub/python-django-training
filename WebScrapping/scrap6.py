from bs4 import BeautifulSoup
import requests
from csv import writer


def scraptheweb(url):
    global new, h, smry, youtube_url, time, author, tags
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    with open('scrap_file.csv', 'w') as file:
        csv_writer = writer(file)
        csv_writer.writerow(['Headlines', 'Summary', 'Youtube URL', 'Date & Time', 'Author', 'Tags'])
        for article in soup.find_all('article'):
            h = article.a.text
            # for article in soup.find_all('article'):
            p = article.find('div', class_='entry-content').p.text
            p = str(p)
            smry = p.split(',')[1].split('.')[0]
            vid_id = article.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
            youtube_url = f"https://youtube.com/watch?v={vid_id}"
            time = article.find('time', class_='entry-time').text
            author = article.find('span', class_='entry-author-name').text
            link = article.find_all('span', class_='entry-categories')
            for each in link:
                each = str(each)
                new = each.split(',')
            for i in new:
                soup = BeautifulSoup(i, 'lxml')
                # print(soup)
            for span in soup.find_all('a'):
                tags = span.text

            csv_writer.writerow([h, smry, youtube_url, time, author, tags])

    # print(h)
    # print('\n')
    # print(smry)
    # print('\n')
    # print(youtube_url)
    # print('\n')
    # print(time)
    # print('\n')
    # print(author)
    # print('\n')
    # print(tags)


scraptheweb('https://www.coreyms.com')
# print(source)
