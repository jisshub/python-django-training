import urllib.request, urllib.parse, urllib.error
link = input('Enter url: ')
fhand = urllib.request.urlopen(link)
for line in fhand:
    print(line.decode().strip())
