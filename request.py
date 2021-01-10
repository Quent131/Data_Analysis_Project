import requests
import json
import pandas as pd
import pickle

url = 'http://127.0.0.1:5000/api/'

data = pickle.load(open('API_data_example.pickle', 'rb'))
data = [data[0].tolist()]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)