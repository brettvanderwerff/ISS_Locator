import requests 
from geopy.geocoders import Nominatim #geopy was downloaded from github

iss = requests.get(url ="http://api.open-notify.org/iss-now.json") #getting coordinates of ISS from API
iss = iss.json()
latitude = (iss['iss_position']['latitude']) #storing latitude of ISS into variable
longitude = (iss['iss_position']['longitude'])#storing longitude of ISS into variable
geolocator = Nominatim()

def issCountryLocator(latitude,longitude):
    x = str(latitude) #making into a string
    y = str(longitude)
    z = x +',' +y #splicing string together since the function below only takes strings not int
    location = geolocator.reverse(z) 
    if type(location.address) == str:
         print(location.address)
    else:
       print("The ISS is currently over water")


issCountryLocator(latitude,longitude)