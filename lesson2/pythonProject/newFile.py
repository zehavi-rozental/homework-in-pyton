import csv
import json
from tkinter.font import names


# 1
def wordInFile():
    word=''
    index=0
    content=''
    with open('file.txt','r') as file:
        content=file.read()
        word=content.split()
        print(len(word))

wordInFile()
# 2
people = [
    ["יוסי", "כהן", 30, "תל אביב"],
    ["מרים", "לוי", 25, "חיפה"],
["חנה", "הורן", 35, "ירושלים"],
    ["שלום", "רוט",30, "מודיעין עילית"],
]

def writeFile(arr):
    with open('files.json','w') as file:
        writer=csv.writer(file)
        writer.writerows(arr)

writeFile(people)
# 3
dictStudent = {"id":1,"name":"Tamar","age":18 }
def writeToJson(dicts):
    with open('data.json','w') as files:
        json.dump(dicts, files)

    with open( 'data.json', 'r') as file:
            data=json.load(file)
            print(data)

writeToJson(dictStudent)