from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
#Get input from user
firstCur=input("Provide first currency: ")
# secondCur=input("Provide second currency: ")

firstCur =firstCur.upper()
# secondCur=secondCur.upper()
# print(firstCur)

#Check if currency is in allowed list
if (firstCur == "EUR") or (firstCur == "USD") or (firstCur == "CHF") or (firstCur == "AUD"):
    print("OK")
else:
    print("Sorry I only know EUR, USD, CHF and AUD")

#Open page
def openPage(currency):
    url="https://www.biznesradar.pl/waluty/nbp/AUD-DOLAR-AUSTRALIJSKI"
    print(url)
    def scraper():
        response = requests.get(url)
        print(response)
        # soup = bs(response.content, 'html.parser')
        # rev_span = soup.findAll("span",attrs={"class","q_ch_act"})
        # for j in range(len(rev_span)):
		# 	# finding all the p tags to fetch only the review text
		#     pagewise_reviews.append(rev_div[j].find("p").text)
        # return all_pages_reviews
    reviews = scraper()
    print(reviews)
    
openPage(firstCur)

# <span class="q_ch_act">3.1215</span>


# base_url = "https://www.consumeraffairs.com/food/dominos.html?page="
# query_parameter = "?page="+str(i) # i represents the page number
