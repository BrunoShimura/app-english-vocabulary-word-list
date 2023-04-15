import pandas as pd
import requests

df = pd.read_csv("vocabulary.csv")
# print(df["word"][1000])

url = "https://wordsapiv1.p.rapidapi.com/words/.22-caliber/pertainsTo"

headers = {
	"X-RapidAPI-Key": "d247523d56msh2df64077db9950cp1a5cebjsnba141debc31e",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
