import re

with open('instagram_accounts.txt', 'r') as f:
    text = f.read()
    pattern = r"([a-zA-Z1-9.][a-z]+_+[a-z][A-Za-z.]*)+"
    result = re.finditer(pattern, text)
    
    for user in result:
        print(user.group())

# i dont understand text for this task, then i have some new solution
pattern = r"[a-z]+_+[a-z]+"
