# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Part 1: Scrape links and images from the IBM website
url_ibm = "http://www.ibm.com"
data_ibm = requests.get(url_ibm).text
soup_ibm = BeautifulSoup(data_ibm, "html5lib")

# Scrape all links
for link in soup_ibm.find_all('a', href=True):
    print(link.get('href'))

# Scrape all images
for link in soup_ibm.find_all('img'):
    print(link)
    print(link.get('src'))

# Part 2: Scrape data from HTML tables on the specified URL
url_color_codes = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data_color_codes = requests.get(url_color_codes).text
soup_color_codes = BeautifulSoup(data_color_codes, "html5lib")

# Find the HTML table
table = soup_color_codes.find('table')

# Get all rows from the table
for row in table.find_all('tr'):
    cols = row.find_all('td')
    color_name = cols[2].string
    color_code = cols[3].text
    print("{} ---> {}".format(color_name, color_code))

# Part 3: Use Pandas to directly read HTML tables from the specified URL
tables = pd.read_html(url_color_codes)
print(tables[0])
