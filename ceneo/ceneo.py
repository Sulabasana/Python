import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.ceneo.pl/49990424")
page = BeautifulSoup(html, 'lxml')
page.prettify()

table = page.find_all('span', class_='value')

for item in table:
    print("Cena ",item.text)
# print(table)
