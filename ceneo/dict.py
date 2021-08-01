import urllib.request
from bs4 import BeautifulSoup
import time

timestr = time.strftime("%d%m%Y")

myItems = {'Płyta':'https://www.ceneo.pl/74881580','Lodówka':'https://www.ceneo.pl/78869466',"Mikrofala":'https://www.ceneo.pl/31934555',"Piekarnik":"https://www.ceneo.pl/49990424","Zmywarka":"https://www.ceneo.pl/49559820"}
for item, link in myItems.items():
    # html = item
    html = urllib.request.urlopen(link)
    page = BeautifulSoup(html, 'lxml')
    page.prettify()

    # table = page.find_all('span', class_='value')
    table = page.find_all('div', class_='product-offer-summary-2020__price-box--with-icon')

    for item1 in table:
        print(item,item1.text.rstrip())
        comb = item,item1.text.rstrip()
        prices = str(comb)
        with open(timestr + '.txt', 'a') as file:
            file.write(f'{prices}\n')
    

    # print(table)
