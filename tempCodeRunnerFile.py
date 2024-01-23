import requests
import json
import pandas as pd
#load the data from the URL.
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")

#Retrieve results using
results2 = json.loads(data2.text)
#Convert json data into pandas data frame.

df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
df3

