import requests
from bs4 import BeautifulSoup

url = "https://trafficinfo.westjr.co.jp/kinki.html"
responce = requests.get(url)
responce.encoding = responce.apparent_encoding
soup = BeautifulSoup()