from bs4 import BeautifulSoup
# first sent a request to the url and so, v get the response
import requests

res = requests.get('https://coreyms.com/')
# here res variable is a response object of the request.
print(res)
# to get the source code ofl that response, use text attribute.
source = res.text
# here source is a string
print(source)
# now we can pass the string as an argument to BeautifulSoup.
soup = BeautifulSoup(source, 'lxml')
print(soup)
