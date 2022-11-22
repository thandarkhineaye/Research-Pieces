# Create index by using elasticsearch api
import requests
import json
index_name="kibana_sample_data_flights"
response = requests.get("http://localhost:9200/" + index_name)
keys = response.json().keys()
for key in keys:
    if key == index_name:
        found = 1
        break
if(found == 1):
    print(f"{index_name}has been found")
else:
    print(f"{index_name}has not been found")
print(response.json().keys())