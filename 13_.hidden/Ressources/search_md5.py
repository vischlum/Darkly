import sys
import requests
from bs4 import BeautifulSoup

_START = "http://"
_END = "/.hidden/"

flags = []

def scrape(site):
    r = requests.get(site)
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("a"):
        href = i.attrs['href']
        url = site + href
        if href == "README":
            f = requests.get(url)
            if f.content not in flags:
                flags.append(f.content)
                print(url)
                print(f.content, '\n')
            break
        elif not href.startswith("../"):
            scrape(url)

if __name__ == "__main__":
    try:
        site = _START + sys.argv[1] + _END
    except IndexError:
        print("Usage: python3 search_md5.py [ip]")
        sys.exit()
    try:
        scrape(site)
    except:
        print("Error during execution.")
        sys.exit()
