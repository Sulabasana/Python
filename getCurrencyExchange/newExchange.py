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
        return("https://www.biznesradar.pl/waluty/nbp/AUD-DOLAR-AUSTRALIJSKI")
    elif(currency == "USD"):
        return("https://www.biznesradar.pl/waluty/nbp/USD-DOLAR")
    elif(currency == "GBP"):
        return("https://www.biznesradar.pl/waluty/nbp/GBP-FUNT-SZTERLING")
    elif(currency == "CHF"):
        return("https://www.biznesradar.pl/waluty/nbp/CHF-FRANK-SZWAJCARSKI")
    elif(currency == "EUR"):
        return("https://www.biznesradar.pl/waluty/nbp/EURO")
       

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
        for j in range(len(rev_span)):
		    # finding all the p tags to fetch only the review text
            pagewise_reviews.append(rev_div[j].find("p").text)
        return all_pages_reviews
    reviews = scraper()
    print(reviews)

openPage(url)




# base_url = "https://www.consumeraffairs.com/food/dominos.html?page="
# query_parameter = "?page="+str(i) # i represents the page number
