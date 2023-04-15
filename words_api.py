import pandas as pd
import requests

df = pd.read_csv("vocabulary.csv")
print(df["word"][1000])

url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + df["word"][1000]

response = requests.request("GET", url)

print(response.text)
