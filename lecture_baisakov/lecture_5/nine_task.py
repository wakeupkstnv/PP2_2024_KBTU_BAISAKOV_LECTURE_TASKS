import re

with open('ei.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    pattern = r"[A-Z][a-z]*(?P<word>.*)\s[A-Z]"
    result = re.sub(pattern, ' ', text)
    print(result)
    