from geopy.geocoders import Nominatim 

def coords(city):
    geolocator = Nominatim(user_agent="Tester") 
    adress = str(city)
    location = geolocator.geocode(adress)
    # debug
    # print(location)
    # print(location.latitude, location.longitude) 
    return location.latitude, location.longitude