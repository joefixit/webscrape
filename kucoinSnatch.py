# import bs4
# https://www.kucoin.com/#/trade/VEN-ETH
# https://www.youtube.com/watch?v=XQgXKtPSzUI
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.kucoin.com/#/trade/VEN-ETH'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


