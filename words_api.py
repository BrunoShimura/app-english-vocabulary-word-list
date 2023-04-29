import pandas as pd
import requests
import json

# function to add to JSON
def write_json(new_data, filename='data.json'):
  with open(filename,'r+') as file:
    # First we load existing data into a dict.
    file_data = json.load(file)
    # Join new_data with file_data inside emp_details
    file_data["words"].append(new_data)
    # Sets file's current position at offset.
    file.seek(0)
    # convert back to json.
    json.dump(file_data, file, indent = 4)

df = pd.read_csv("vocabulary.csv")
url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + "office"
response = requests.request("GET", url)
data = json.loads(response.text)[0]

all_audio = []
all_definitions = []
all_exemples = []
all_synonyms = []

# mp3 pthonetcs audio
for i in data['phonetics']:
  if (i["audio"] != ""):
    all_audio.append(i["audio"])

# examples
for i in data['meanings']:
    for j in i['definitions']:
      if len(j) > 3:
        all_definitions.append(j['definition'])
        all_exemples.append(j['example'])
    for k in i['synonyms']:
      all_synonyms.append(k)

# python object to be appended
y = {
  "id": 1,
  "definitions": all_definitions,
  "exemples": all_exemples,
  "synonyms": all_synonyms,
  "audio": all_audio,
}
     
write_json(y)
