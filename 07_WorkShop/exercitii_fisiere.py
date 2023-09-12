'''

Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file

'''

f = open("hello.txt", "r")
text = f.read()
f.close()
print(text)

print('*' * 50)
''' 
2 Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
Display the new contents of the file.
'''
list = ['\nGo', 'Kotlin', 'Swift']
with open("hello.txt", "a") as f:
    for line in list:
        f.write(line)
f = open("hello.txt", "r")
text = f.read()
f.close()
print(text)
print('*' * 50)
'''
3
Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).

'''
with open("hello.txt", "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines, start=1):
        if index % 2 == 1:
            print(line.strip())
print('*' * 50)
'''
4 Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, 
'''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for index, element in enumerate(alphabet):
    with open(f"{element}.txt", 'w') as f:
        f.write(f"My name is letter {element}\n")
        t = ""
        if index == 0 or index == 20:
            t = "'st"
        elif index == 1 or index == 21:
            t = "'nd"
        elif index == 2 or index == 22:
            t = "`rd"
        else:
            t = "th"
        f.write(f"And I`m the {index + 1}{t} letter of the alphabet")
print('*' * 50)
'''
5
Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
Read the file using Python’s `csv` standard library, and display it in the terminal as a 
table, using the options for string formatting from Python:
id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu		21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa			29	9.0

'''
import csv

with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    hedder = next(reader)
    print(f'{hedder[0]:5}{hedder[1]:15}{hedder[2]:15}{hedder[3]:10}{hedder[4]:5}')
    print('-' * 50)
    for row in reader:
        print(f"{row[0]:5}{row[1]:15}{row[2]:15}{row[3]:5}{row[4]:10}")
print('*' * 50)
import pandas as pd

df = pd.read_csv("students.csv")
print(df.to_string())

print('*' * 50)
'''
6
Read again the information from the csv file above, store it all in a list of data,
 and then write a new file, called “students.json”, which will contain a valid JSON
  object. Use the following format for each student (and use Python’s standard JSON module):
[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5	
	},
	...
]

'''

import csv
import json
import pprint

students = []
with open("students.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        student = {
            "id": int(row["id"]),
            "fnsme": row["fname"],
            "lname": row["lname"],
            "age": int(row["age"]),
            "grade": float(row["grade"])
        }
        students.append(student)
print(students)
with open("students.json", "w") as jsonfile:
    json.dump(students, jsonfile, indent=4)
with open("students.json", "r") as jsonfile:
    students = json.load(jsonfile)
    for student in students:
        print(students)

'''
Create a new PyCharm project. Make sure it has a virtualenv. Install all the following
packages from PYPI:
behave
behave-html-formatter
requests
selenium
webdriver-manager
Use pip to create a `requirements.txt` file. Send your project to a colleague and ask 
them to install all dependencies using pip.

'''