import re
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('article')

# scrap the video_id from src attribute.
src = article.find('iframe', class_='youtube-player')['src']

# so first the split the src based on character '/'. which gives a list of values.
list_items = src.split('/')

# now video_id is at index 4.
vid_id = src.split('/')[4]

# now again split based on '?' and access the index 0.
vid_id = vid_id.split('?')[0]
print(vid_id)

# now we can create a youtube link with that id.
url = f'https://youtube.com/watch?v={vid_id}'
print(url)
