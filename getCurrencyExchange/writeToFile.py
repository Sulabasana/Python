from datetime import date
from getCurrencyExchange import *

today = date.today()
d1 = today.strftime("%d.%m.%Y")
print("Today's date:", d1)
print("Exchange rate is: ", getRate())
rate=getRate()
with open('file.txt','a') as f:
    f.write(f"{d1};{rate}\n")
    
