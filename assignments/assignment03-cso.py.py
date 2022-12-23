import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

dataset = requests.get(url)

with open("cso.json", "w") as outfile:
    json.dump(dataset.json(), outfile)