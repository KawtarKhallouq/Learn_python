import pandas as pd
import requests

import json
#obtain te fruityvice api data 
data = requests.get("https://fruityvice.com/api/fruit/all")

#retrieve result
results = json.loads(data.text)

#convert json data to pandas data frame
pd.DataFrame(results)
#The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
df2

# The family and genus of a cherry
cherry = df2.loc[df2["name"] == 'Cherry']
family_cherry, genus_cherry = cherry.iloc[0]['family'], cherry.iloc[0]['genus']


# How many calories are contained in a banana
banana = df2.loc[df2["name"] == 'Banana']
cal_banana = banana.iloc[0]['nutritions.calories']

print(f"Family of Cherry: {family_cherry}")
print(f"Genus of Cherry: {genus_cherry}")
print(f"Calories in Banana: {cal_banana}")


