# import the elasticsearch client library
from elasticsearch import Elasticsearch
import io
# connect elastic search localhost 9200 port
es = Elasticsearch([{"host":"localhost", "port":9200}])
print(es.ping())
# search specific index
index = "kibana_sample_data_flights"
try:
    response = es.search(index=index)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))

# search specific index
index = "november*"
try:
    response = es.search(index=index)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))