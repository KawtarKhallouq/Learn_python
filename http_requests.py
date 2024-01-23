import requests
import os
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r = requests.get(url)

print(r.status_code)
print(r.request.headers)
print("request body:", r.request.body)
header = r.headers
print(header['date'])
print(header['Content-Type'])
print(r.encoding)
print(r.text[0:100])

# Use single quotation marks for defining string
url_image = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r_image = requests.get(url_image)
print(r_image.headers['Content-Type'])
path = os.path.join(os.getcwd(), 'image.png')

with open(path, 'wb') as f:
    f.write(r_image.content)

Image.open(path)
