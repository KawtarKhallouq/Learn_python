from random import randint as rnd

memReg = '/members.txt'
exReg = '/inactive.txt'
fee = ('yes', 'no')

def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))

genFiles(memReg, exReg)

def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as currentFile:
        with open(exMem, 'a+') as exFile:
            members = currentFile.readlines()
            inactive_members = [member for member in members[1:] if 'no' in member]
            exFile.writelines(inactive_members)

            currentFile.seek(0)
            currentFile.write(members[0])
            currentFile.writelines([member for member in members[1:] if 'no' not in member])

# The code below is to help you view the files.
# Do not modify this code for this exercise.
headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(headers + readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(headers + readFile.read())

def testMsg(passed):
    if passed:
        return 'Test Passed'
    else:
        return 'Test Failed'

testWrite = "/testWrite.txt"
testAppend = "/testAppend.txt"
passed = True

genFiles(testWrite, testAppend)

with open(testWrite, 'r') as file:
    ogWrite = file.readlines()

with open(testAppend, 'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite, testAppend)
except:
    print('Error')

with open(testWrite, 'r') as file:
    clWrite = file.readlines()

with open(testAppend, 'r') as file:
    clAppend = file.readlines()

# checking if the total number of rows is the same, including headers
if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False

for line in clWrite:
    if 'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match the original file")
            passed = False

print("{}".format(testMsg(passed)))
