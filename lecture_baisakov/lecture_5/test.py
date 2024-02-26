import re
'''
with open('parsing_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    pattern = r"\n(?P<num>[0-9]+).\n(?P<name>.+)\n"
    result = re.finditer(pattern, text)
    
    for i in result:
        print(i.group('num'), i.group('name'))
        
f.close()
'''

'''
with open('instagram_accounts.txt', 'r') as f:
    text = f.read()
    pattern = r"(@[a-zA-z.]*)+"
    result = re.finditer(pattern, text)
    
    for user in result:
        print(user.group())
'''

with open('1984.txt', 'r') as f:
    text = f.read()
    pattern = r"[Ww][Aa][rR]"
    result = re.sub(pattern, 'DICK', text)
    print(result)