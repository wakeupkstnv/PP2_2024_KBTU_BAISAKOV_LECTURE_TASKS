import re

with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    pattern = r"[ ]+[A-Z][a-z]+"
    result = re.finditer(pattern, text)
    for word in result:
        print(word.group())
        
   