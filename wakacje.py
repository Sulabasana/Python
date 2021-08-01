import urllib.request
from bs4 import BeautifulSoup

link = "https://www.wakacje.pl/oferty/egipt/hurghada/hurghada/sea-gull-beach-resort-hurghada-605155.html?od-2021-05-27,7-dni,all-inclusive,z-wroclawia,sr3,2dorosle-1dziecko-20151125"

html = urllib.request.urlopen(link)
page = BeautifulSoup(html, 'lxml')
page.prettify()
# print(page.prettify())

# with open('file.txt', 'w') as f:
#     f.write(str(page))

    # table = page.find_all('span', class_='value')
table = page.find_all('span', {"class":'sc-10eoahi-6 GABzG'})
print(table)

for item1 in table:
    # print("Cena",item1.text.rstrip())
    print(item1.text.rstrip())
    # print(table)
