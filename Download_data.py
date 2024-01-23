import urllib.request

# Download file using urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'example1.txt'
urllib.request.urlretrieve(url, filename)

# Read the file using with open
with open(filename, 'r') as file1:
    # Print file information
    print("File Name:", file1.name)
    print("File Mode:", file1.mode)

    # Read the entire file
    file_content = file1.read()
    print("File Content:")
    print(file_content)

    # Read specific characters
    print("First four characters:", file1.read(4))

    # Read one line
    print("First line:", file1.readline())

    # Iterate through the lines
    print("Iterating through the lines:")
    for i, line in enumerate(file1):
        print(f"Iteration {i}: {line}")

    # Read all lines and save as a list
    file1.seek(0)  # Reset file pointer to the beginning
    file_as_list = file1.readlines()

# Print specific lines from the list
print("Specific lines from the list:")
print("First line:", file_as_list[0])
print("Second line:", file_as_list[1])

# Verify if the file is closed
print("Is the file closed?", file1.closed)
