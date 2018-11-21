import re

a = 44421
b = str(a)

# matchObj = re.match(r'^([0-9])+', a)

matchObj2 = re.match(r'(\d)+', b)

# print(matchObj.group())
print(matchObj2.group())