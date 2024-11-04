import re

# exo1

def onlyAlphabet2 (text):
    return bool(re.match('^[a-zA-Z]+$',text))

txt = input("enter a text :")
print(onlyAlphabet2(txt))