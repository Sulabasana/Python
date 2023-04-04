from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from datetime import date
import requests


url = "https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ZLOTO"

def openPage(ending):
    # print(ending)
    def scraper():
        response = requests.get(ending)
        # print(response)
        soup = bs(response.content, 'html.parser')
        rev_span = soup.find("div",attrs={"class","profilLast"})
        # print(rev_span)
        goldValue=rev_span.text
        return goldValue
        # print(goldValue)
       
    reviews = scraper()
    return reviews
    # print(reviews)
# openPage(url)

goldRate = openPage(url)

today = date.today()
d1 = today.strftime("%d.%m.%Y")
print("Today's date:", d1)
print("Gold rate is: ", goldRate)
# rate=rateCurrency
with open('goldRate.txt','a') as f:
    f.write(f"{d1};{goldRate}\n")
    