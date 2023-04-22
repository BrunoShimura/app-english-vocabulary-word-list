import pandas as pd
import requests
import json
df = pd.read_csv("vocabulary.csv")


#url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + "dog"

#response = requests.request("GET", url)

#data = json.loads(response.text)


#df_shuffled=df.sample(frac=1).reset_index(drop=True)
#df_shuffled.to_csv('output.csv')
#print(df_shuffled)


# Opening JSON file
f = open('example.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

"""

# all definitions len(data['meanings'][0]['definitions'])
for i in range(0, 2):
  if data['meanings'][0]['definitions'][i]['definition']:
    print(data['meanings'][0]['definitions'][i]['definition'])

# mp3 pthonetcs audio
for i in data['phonetics']:
  print(i["audio"])

# synonymous
print(data['meanings'][0]['synonyms'])

"""


# examples
for i in data['meanings']:
    for j in i['definitions']:
      if len(j) > 3:
        print("Definition: "+j['definition'])
        print("Example: "+j['example'])
        print("\n")
    print(i['synonyms'])

# Closing file
f.close()


