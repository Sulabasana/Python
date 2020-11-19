import urllib.request
from bs4 import BeautifulSoup

myItems = ['https://www.ceneo.pl/74881580','https://www.ceneo.pl/78869466','https://www.ceneo.pl/31934555']
for item in myItems:
    # html = item
    html = urllib.request.urlopen(item)
    page = BeautifulSoup(html, 'lxml')
    page.prettify()

    # table = page.find_all('span', class_='value')
    table = page.find_all('div', class_='product-offer-summary-2020__price-box--with-icon')

    for item1 in table:
        print("Cena",item1.text.rstrip())
    # print(table)
