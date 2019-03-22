# ul00.py

from urllib.request import urlopen

# url = 'https://www.naver.com/'
url = 'https://www.daum.net/'
html = urlopen(url)
status = html.getheaders()
for s in status:
    print(s)

#print(html.read())