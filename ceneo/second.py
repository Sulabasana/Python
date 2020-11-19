import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.ceneo.pl/78869466")
page = BeautifulSoup(html, 'lxml')
page.prettify()

# table = page.find_all('span', class_='value')
table = page.find_all('div', class_='product-offer-summary-2020__price-box--with-icon')

for item in table:
    print("Cena ",item.text)
# print(table)
