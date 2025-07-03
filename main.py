import subprocess, os
from subprocess import run as run
import json
print("Creating depandancies.txt")
with open("dependancies.txt", "w") as f:
    run('pipdeptree', stdout=f)
if os.path.isfile("./dependancies.txt"):
    print("File created...")
else:
    raise Exception("file not created")

print("Creating licences.txt")
with open("licenses.txt", "w") as f:
    run(['pip-licenses'], stdout=f)
if os.path.isfile("./licenses.txt"):
    print("File created...")
else:
    raise Exception("file not created")

# Parse licenses.txt to licenses.json
myList = []
with open("licenses.txt", "r") as fileIn:
    fileIn.readline()
    temp_bool = False
    for x in fileIn:
        if temp_bool:
            temp = x.split()
            temp_dict = {"name": temp[0],"version":temp[1], "license":" ".join(temp[2::])}
            myList.append(temp_dict)
        temp_bool = not temp_bool
try:
    with open("licenses.json","w") as f:
        json.dump(myList, f, indent=4)
except:
    print(f'An unexpected error occured with parsing to json: {Exception}')



