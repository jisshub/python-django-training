from bs4 import BeautifulSoup

with open('index.html') as index_file:
    soup = BeautifulSoup(index_file, 'lxml')

list_element = soup.find_all('li')
for a in list_element:
    print(a.text)

print('###########################################################################')
print('###########################################################################')
h1_tag = soup.find_all('h1')
for t in h1_tag:
    print(t.text)
