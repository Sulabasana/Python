from datetime import date
from datetime import datetime


today = date.today()
print (f"Today's date is", today)
week = datetime.today().strftime("%V")
print("Week number is " + week)