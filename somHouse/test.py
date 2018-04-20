import urllib.request
def download(url): 
    return urllib.request.urlopen(url).read() 

import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
    print(html)

download("https://www.awwwards.com")