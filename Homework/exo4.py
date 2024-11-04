import re

def validate_pass(text):
    if len(text)<10:
        return "False1"
    if not re.search(r"[A-Z]",text):
        return "False2"
    if not re.search(r"[a-z]",text):
        return "False3"
    if not re.search(r"\d",text):
        return  "False4"
    if not re.search(r"[\!\@\#\$\%\^\&\*]",text):
        return "False5"
    return True

print(validate_pass("Secure!2021"))
    