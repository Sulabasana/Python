import urllib.request
from bs4 import BeautifulSoup
import time

timestr = time.strftime("%d%m%Y")

myItems = {"Realme 8":'https://www.ceneo.pl/105868112','Realme 8 Pro':'https://www.ceneo.pl/105881227', "Polar": "https://www.ceneo.pl/93287298", "Pocco":"https://www.ceneo.pl/105945470;0280-0.htm", "Denon":"https://www.ceneo.pl/94434916"}
for item, link in myItems.items():
    # html = item
    html = urllib.request.urlopen(link)
    page = BeautifulSoup(html, 'lxml')
    page.prettify()

    # table = page.find_all('span', class_='value')
    table = page.find('span', class_='value')

    for item1 in table:
        print(item,item1)
        comb = item +' - '+ item1 + " zł"
        prices = str(comb)
        with open(timestr + '.txt', 'a') as file:
            file.write(f'{prices}\n')
    

    # print(table)
