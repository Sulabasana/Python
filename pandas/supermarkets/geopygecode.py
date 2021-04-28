# from geopy.geocoders import Nominatim
# nom = Nominatim()
# change them to these
# import pandas
# from geopy.geocoders import ArcGIS
# nom = ArcGIS()
# # The rest of the code remains the same.
# adress1= nom.geocode("Rynek 9/11,Wrocław, Poland")
# lat = adress1.latitude
# lon = adress1.longitude
# print(adress1, lat, lon)
import pandas
from geopy.geocoders import ArcGIS
nom = ArcGIS()

df=pandas.read_csv("supermarkets.csv")
df["Address"]=df["Address"]+','+ df["City"] + ',' + df["State"] + ','+ df["Country"]
# print(df)

df["Coordinates"] = df["Address"].apply(nom.geocode)
# print(df.Coordinates[0])
df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)

