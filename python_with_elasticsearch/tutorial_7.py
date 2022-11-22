# Create index by using elasticsearch api
import requests

response = requests.put("http://localhost:9200/test_index_using_api")
print(response.text)