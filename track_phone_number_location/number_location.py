import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

### Need to create account at OpenCageGeocode ###
### After finished sign up, you will get API Key ###
### Use that key to following ###
OPENCAGE_KEY = ''

# get input phone number from user   
ph_number = input("Enter phone number (+0123456789):")

# convert input phone number
parseNumber = phonenumbers.parse(ph_number)

# get location
yourLocation = geocoder.description_for_number(parseNumber, "en")

# get service provider
serviceProvider = carrier.name_for_number(parseNumber, "en")

# initialize location with opencage
geocoder = OpenCageGeocode(OPENCAGE_KEY)
query = str(yourLocation)
results = geocoder.geocode(query)
#latitude and long
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Map
myMap = folium.Map(location=[lat, lng], zoom_start=9)
# create marker on map
folium.Marker([lat, lng], popup= yourLocation).add_to(myMap)

# save map in HTML File
myMap.save('mylocation.html')

# print out
print(yourLocation)
print(serviceProvider)
#print(results)
print(lat,lng)