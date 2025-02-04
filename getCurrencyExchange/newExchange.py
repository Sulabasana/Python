from locale import currency
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests

#Get input from user
firstCur = input("Provide first currency: ")
# secondCur=input("Provide second currency: ")
currencyEnd = ""
firstCur = firstCur.upper()

#Check if currency is in allowed list
if (firstCur == "EUR") or (firstCur == "USD") or (firstCur == "CHF") or (firstCur == "AUD") or (firstCur == "GBP"):
    print("OK")
else:
    print("Sorry I only know EUR, USD, CHF, GBP and AUD")
  
# Preparing URL based on currency
def prepareURL(currency):
    # currencyEnd 
    if(currency == "AUD"):
        return("https://www.biznesradar.pl/notowania/AUD-DOLAR-AUSTRALIJSKI")
    elif(currency == "USD"):
        return("https://www.biznesradar.pl/notowania/USD-DOLAR")
    elif(currency == "GBP"):
        return("https://www.biznesradar.pl/notowania/GBP-FUNT-SZTERLING")
    elif(currency == "CHF"):
        return("https://www.biznesradar.pl/notowania/CHF-FRANK-SZWAJCARSKI")
    elif(currency == "EUR"):
        return("https://www.biznesradar.pl/notowania/EURO")
       

# print(prepareURL(firstCur))
url = prepareURL(firstCur)
# print(prepareURL(firstCur))
# Open page
def openPage(ending):
    # print(ending)
    def scraper():
        response = requests.get(ending)
        # print(response)
        soup = bs(response.content, 'html.parser')
        rev_span = soup.findAll("span",attrs={"class","q_ch_act"})
        # print(rev_span)
        for i in range(len(rev_span)):
            if i == 1:
                # print(rev_span[0])
                rev_span = rev_span[0].text
                # print(rev_span)
                #finding all the p tags to fetch only the review text
            # pagewise_reviews.append(rev_div[j].find("p").text)
        # return all_pages_reviews
        # print("1 " + firstCur + " is " + rev_span + " PLN")
        return("1 " + firstCur + " is " + rev_span + " PLN")
    reviews = scraper()
    return reviews
    # print(reviews)

openPage(url)
rateCurrency = openPage(url)




# base_url = "https://www.consumeraffairs.com/food/dominos.html?page="
# query_parameter = "?page="+str(i) # i represents the page number
