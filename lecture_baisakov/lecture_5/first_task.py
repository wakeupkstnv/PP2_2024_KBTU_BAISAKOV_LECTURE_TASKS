import re

with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    pattern = r"ab*"
    result = re.findall(pattern, text)
    print(result)
