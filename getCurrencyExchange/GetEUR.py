from locale import currency
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
from datetime import date


url = "https://www.biznesradar.pl/notowania/EURO"
       

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
        return("1 EUR is " + rev_span + " PLN")
    reviews = scraper()
    return reviews
    # print(reviews)

openPage(url)
rateCurrency = openPage(url)


today = date.today()
d1 = today.strftime("%d.%m.%Y")
print("Today's date:", d1)
print("Exchange rate is: ", rateCurrency)
rate=rateCurrency
with open('EURRate.txt','a') as f:
    f.write(f"{d1};{rate}\n")
    





# base_url = "https://www.consumeraffairs.com/food/dominos.html?page="
# query_parameter = "?page="+str(i) # i represents the page number
