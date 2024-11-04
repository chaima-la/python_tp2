import re


def findDegits(text):
    return re.findall(r"\d",text)
 

text = input("enter a text: ")
print(findDegits(text))