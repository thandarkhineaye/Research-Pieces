# import the elasticsearch client library
from elasticsearch import Elasticsearch
import io
# connect elastic search localhost 9200 port
es = Elasticsearch([{"host":"localhost", "port":9200}])
print(es.ping())

# index creation in bulk using input file
with io.open("input.txt", "r", encoding="utf-8")as f1:
    data = f1.read()
    f1.close()
# prepare read data by newline
data = data.split("\n")
# create index with sequence
for i in data:
    response = es.indices.create(index=i)
    print(response)