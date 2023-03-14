# from datetime import date
# from getCurrencyExchange import *

# today = date.today()
# d1 = today.strftime("%d.%m.%Y")
# print("Today's date:", d1)
# print("Exchange rate is: ", getRate())
# rate=getRate()
# with open('file.txt','a') as f:
#     f.write(f"{d1};{rate}\n")

from datetime import date
from newExchange import *

today = date.today()
d1 = today.strftime("%d.%m.%Y")
print("Today's date:", d1)
print("Exchange rate is: ", rateCurrency)
rate=rateCurrency
with open('currencyRate.txt','a') as f:
    f.write(f"{d1};{rate}\n")
    
