# import the elasticsearch client library
from elasticsearch import Elasticsearch
# connect elastic search localhost 9200 port
es = Elasticsearch([{"host":"localhost", "port":9200}])
print(es.ping())

# create index
# es.indices.create(index="tutorial-20221122")

# display all indices
indices = es.indices.get_alias("*")
for index in indices:
    print(index)
