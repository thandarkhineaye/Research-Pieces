# import the elasticsearch client library
from elasticsearch import Elasticsearch
import pandas as pd
# import Python's json library to format JSON responses
import json

try:

    # declare a client instance of the Python Elasticsearch library
    client = Elasticsearch("http://localhost:9200")

    # pass client object to info() method
    elastic_info = Elasticsearch.info(client)
    # マッピング情報の取得
    #response = client.indices.get_mapping(index="test_index1")
    response = client.search(index='kibana_sample_data_flights')
    #print ("Cluster info:", json.dumps(elastic_info, indent=4 ))
    print (json.dumps(response, indent=2))

    # export response with json file
    path = 'test_json.json'
    json_file = open(path, mode="w")
    json.dump(response, json_file, indent=2, ensure_ascii=False)
    json_file.close()
    # conver json to excel file
    df = pd.read_json(path)
    df.to_excel('test_excel.xlsx')

except Exception as err:
    print ("Elasticsearch client ERROR:", err)
    client = None