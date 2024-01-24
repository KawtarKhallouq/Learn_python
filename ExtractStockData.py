import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')

netflix_dataframe = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

# First, we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Create a new DataFrame for each row and concatenate it to the main DataFrame
    row_data = pd.DataFrame({"Date": [date], "Open": [Open], "High": [high], "Low": [low], "Close": [close], "Adj Close": [adj_close], "Volume": [volume]})
    netflix_dataframe = pd.concat([netflix_dataframe, row_data], ignore_index=True)

# Display the DataFrame
print(netflix_dataframe.head())
