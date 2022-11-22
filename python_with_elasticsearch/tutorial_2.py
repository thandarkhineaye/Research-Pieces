# import the elasticsearch client library
from elasticsearch import Elasticsearch
# connect elastic search localhost 9200 port
es = Elasticsearch([{"host":"localhost", "port":9200}])
print(es.ping())

# create index with sequence
index_basename = "november"
for i in range(1, 11):
    response = es.indices.create(index=index_basename + "_" +str(i))
    print(response)