#pip3 install geopy

from geopy.geocoders import Nominatim
import time
from pprint import pprint

# instantiate a new Nominatim client
app = Nominatim(user_agent="tutorial")

# get location raw data
location = app.geocode("Wielka Sowa, Poland").raw
# print raw data
pprint(location)