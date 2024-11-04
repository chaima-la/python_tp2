import re

def passwordValid(txt):
    if len(txt) <8 :
        return False
    if not re.search(r"[a-z][A-Z]",txt):
        return False
    if not re.search(r"[0-9]",txt):
        return False
    if not re.search(r"[!@#$%^&*]", txt):
        return False
    return True

print(passwordValid("kH3!djhgfhdfg"))