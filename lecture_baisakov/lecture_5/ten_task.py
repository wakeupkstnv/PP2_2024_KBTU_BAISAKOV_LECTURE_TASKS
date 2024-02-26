import re

with open('ei.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    pattern = r"([A-Z])"
    result = re.sub(pattern, r"_ \1", text).strip()
    
    print(re.sub(' ', '', result))