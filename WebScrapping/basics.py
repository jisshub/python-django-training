# BeautifulSoup Documentation link:
'''https://www.crummy.com/software/BeautifulSoup/bs4/doc/'''

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.

# import the libraries.

from bs4 import BeautifulSoup
import requests

with open('data.html') as html_file:
    # pass that file to a beautifulsoup
    soup = BeautifulSoup(html_file, 'lxml')
    # here v pass the html file and specify the parser as lxml
    # now we parsed the html file using lxml parser and v have a soup variable which is
    # a beautifulsoup object.

print(soup)

# here v get the title element of the file
print(soup.title)
#     to get the text value of title use, text attribute
print(soup.title.text)
# to get the first div of the page
print(soup.div)
# to get the footer
print(soup.footer)

# to get the div element with class article.
# use find method and pass two args. one is div and second is class_.
print(soup.find('div', class_='article1'))

# to get the div with an id article3.
print(soup.find('div', id='article3'))

print('########################################################')
# to get the list of p with same class.
# use find_all gives the list that contains p with class para-1
print(soup.find_all('p', class_='para1'))

# get a list of all h2 elements.
print(soup.find_all('h2'))

# get a alist of all anchor elements.
print(soup.find_all('a'))
