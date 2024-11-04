import re

def hashtags(txt):
    return re.findall(r"#\w+",txt)


print(hashtags("Here are some hashtags: #Python, #coding, and #OpenAI!"))