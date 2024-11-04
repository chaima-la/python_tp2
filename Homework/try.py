import re

s = "abc hjgb wxcbbbbnf"
match = re.findall(r"b?\w*",s)

print(match)
