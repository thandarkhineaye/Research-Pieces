# import the elasticsearch client library
from elasticsearch import Elasticsearch
import io
# connect elastic search localhost 9200 port
es = Elasticsearch([{"host":"localhost", "port":9200}])
print(es.ping())

# search and display the index names based on the given search pattern
index_pattern = "t"
response = es.indices.get_alias(index_pattern)
if len(response) > 0:
    for index in response:
        delete_response = es.indices.delete(index=index)
        print(delete_response)
else:
    print("no index has been found")