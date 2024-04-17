import json
import pandas as pd 

with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)

new_csv = []

for p in data[:5]:
        new_csv.append([p['name'], p['html_url'], p['updated_at'], p['visibility']])

pd.DataFrame(new_csv).to_csv('/workspace/json-practice/lab8/chacon.csv', index=False, header=False)
