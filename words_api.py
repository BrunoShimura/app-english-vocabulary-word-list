import pandas as pd
import requests
import json
df = pd.read_csv("vocabulary.csv")


#url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + df["word"][1000]

#response = requests.request("GET", url)

#test = json.loads(response.text)
df_shuffled=df.sample(frac=1).reset_index(drop=True)
df_shuffled.to_csv('output.csv')
print(df_shuffled)
"""

# Opening JSON file
f = open('example.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# for in definitions and exemples
for i in range(0, len(data['meanings'][0]['definitions'])):
  if data['meanings'][0]['definitions'][i]['definition']:
    print(data['meanings'][0]['definitions'][i]['definition'])

for i in data['phonetics']:
  print(i["audio"])
  
t = data['meanings'][0]['definitions'][0]
for i in json.loads(t).iteritems():

  print(t)

# Closing file
f.close()
"""