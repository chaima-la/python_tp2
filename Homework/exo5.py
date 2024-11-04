import re
def extract_hashtag(text):
    return re.findall(r"\B#\w+",text)


print(extract_hashtag("dsjfjg #hjg #jsdgf #ksdhgf ksdj"))