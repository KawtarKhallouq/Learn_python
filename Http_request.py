import requests
import os
from PIL import Image
from IPython.display import IFrame

# Make a GET request to www.ibm.com
url = 'https://www.ibm.com/'
r = requests.get(url)

# View the status code
print("Status Code:", r.status_code)

# View the request headers
print("Request Headers:", r.request.headers)

# View the request body
print("Request Body:", r.request.body)

# View the HTTP response header
header = r.headers
print("Response Headers:", header)

# Obtain the date the request was sent
print("Date:", header['date'])

# Content-Type indicates the type of data
print("Content-Type:", header['Content-Type'])

# Check the encoding
print("Encoding:", r.encoding)

# Display the HTML in the body (first 100 characters)
print("HTML Body:", r.text[0:100])

# Make a GET request for an image
image_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
image_response = requests.get(image_url)

# Save the image to a file
image_path = os.path.join(os.getcwd(), 'image.png')
with open(image_path, 'wb') as f:
    f.write(image_response.content)

# View the image
Image.open(image_path)

# Download a file
file_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
file_response = requests.get(file_url)
with open('Example1.txt', 'wb') as file:
    file.write(file_response.content)

# Get Request with URL Parameters
url_get = 'http://httpbin.org/get'
payload = {"name": "Joseph", "ID": "123"}
get_response = requests.get(url_get, params=payload)
print("GET Request URL:", get_response.url)
print("Request Body:", get_response.request.body)
print("Status Code:", get_response.status_code)
print("Response Text:", get_response.text)
print("Content-Type:", get_response.headers['Content-Type'])
print("Response JSON:", get_response.json()['args'])

# Post Requests
url_post = 'http://httpbin.org/post'
post_response = requests.post(url_post, data=payload)
print("POST Request URL:", post_response.url)
print("GET Request URL:", r.url)
print("POST Request Body:", post_response.request.body)
print("GET Request Body:", r.request.body)
print("Form Data:", post_response.json()['form'])
