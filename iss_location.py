from geopy.geocoders import Nominatim #Imports go in alphabetical order.
import requests

def get_iss_response(): # Docstrings are added to each function. Script is refactored so each function now only does one thing.
    '''Function gets a JSON response from an API call to an ISS tracking site.
    '''
    iss = requests.get(url ="http://api.open-notify.org/iss-now.json")
    return iss.json()

def get_iss_coordinates(iss_response):
    '''Function obtains latitude and longitude coordinates from return of get_iss_response function.
    '''
    latitude = (iss_response['iss_position']['latitude'])
    longitude = (iss_response['iss_position']['longitude'])
    return latitude, longitude

def get_country_location(latitude,longitude):
    '''Function takes latitude and longitude coordinates of ISS location as arguments and returns the country name
    corresponding to those coordinates.
    '''
    transform_lat_long = str(latitude) + ',' + str(longitude) #Refactored for brevity.
    geolocator = Nominatim()
    location = geolocator.reverse(transform_lat_long)
    if type(location.address) == str:
        return(location.address)
    else:
        return('The ISS is currently over water.')

def run():
    '''Run function that calls all functions in script. Function prints the country name that the ISS is currently over.
    '''
    iss_response = get_iss_response()
    latitude, longitude = get_iss_coordinates(iss_response)
    country_location = get_country_location(latitude, longitude)
    print(country_location)

if __name__ == '__main__': #Makes it so you can import module methods on an individual basis. 
    run()

