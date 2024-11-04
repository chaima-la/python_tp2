import re

def capi (txt):
    return re.findall(r"\b[A-Z]\w*",txt)


print(capi("kqdsg hdg Jjhsdf Osdhfg bhKjg"))