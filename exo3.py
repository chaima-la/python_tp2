import re

def validEmail (emailList):
    for txt in emailList:
        isValid = re.search(r"@.+\.com$",txt)
        if isValid:
            print(f"{txt}the email is valid")
 

validEmail(["sldjsdlkc@sdjddj.com","skjdfhk","kjqd@gmail.com"])
