# from forex_python.converter import CurrencyRates

# c = CurrencyRates()

# print(c.get_rate('EUR', 'PLN'))
from forex_python.converter import CurrencyRates

c = CurrencyRates()

firstCur=input("Provide first currency: ")
secondCur=input("Provide second currency: ")

firstCur =firstCur.upper()
secondCur=secondCur.upper()

# print(firstCur)
# print(secondCur)
print(c.get_rate(firstCur, secondCur))

