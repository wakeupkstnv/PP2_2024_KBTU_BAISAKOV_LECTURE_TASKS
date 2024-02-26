import re

text = '''
some_variable
_count_variable
sum_of_column
i_love_PYTHON
'''

pattern = r".+"
result = re.finditer(pattern, text)

for i in result:
    pattern_for_snake_to_camel = r"_*(?P<var>[^_]+)[_]*\s*"
    result_snake_to_camel = re.findall(pattern_for_snake_to_camel, i.group())
    new_result = [j.capitalize() if j != result_snake_to_camel[0] else j for j in result_snake_to_camel]
    print("".join(new_result))
