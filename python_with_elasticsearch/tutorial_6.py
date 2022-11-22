# import the elasticsearch client library
from elasticsearch import Elasticsearch
import io
# connect elastic search localhost 9200 port
es = Elasticsearch([{"host":"localhost", "port":9200}])
print(es.ping())

# delete elasticsearch index by using input file
with io.open("input.txt", "r", encoding="utf-8")as f1:
    data = f1.read()
    f1.close()
# prepare read data by newline
data = data.split("\n")
# create index with sequence
for i in data:
    try:
        response = es.indices.delete(index=i)
        print(response)
    except Exception as e:
        print("error occured while deleting index")