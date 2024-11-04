import re

def validate(txt):
    pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$"
    if re.match(pattern,txt):
        month , day , year = map(int, txt.split('-'))
        if (month in {4, 6, 9, 11} and day > 30):
            return False
        if(month == 2):
            if(year%4 !=0 and day>28) or (year%4 ==0 and day>29):
                return False
        return True
    else:
        return False
    

print(validate("02-27-2000"))
print(validate("02-29-2000"))
print(validate("02-29-2001"))
print(validate("04-31-2021"))
print(validate("13-01-2021"))