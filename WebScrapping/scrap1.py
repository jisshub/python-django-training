from bs4 import BeautifulSoup
# first sent a request to the url and so, v get the response
import requests

res = requests.get('https://coreyms.com/')
# here res is a response object of the request.
print(res)
# to get the source code of the that response, use text attribute.
source = res.text
# here source is a string
print(source)
