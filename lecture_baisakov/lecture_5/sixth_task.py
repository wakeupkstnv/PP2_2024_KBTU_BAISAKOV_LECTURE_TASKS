import re

with open('sample.txt', 'r') as f:
    text = f.read()
    pattern = r"[\s.,]"
    result = re.sub(pattern, '..', text)
    print(result)