import re

def checkIO(password):
    if re.search(r'^[a-zA-Z0-9]+$', password):
        if re.search(r'[a-z]+', password) and re.search('[A-Z]+', password) \
                and re.search('[0-9]+', password) and 16 >= len(password) >= 8:
            return True
        else:
            return False
    return 'INPUT ERROR'

password = input()
x = checkIO(password)
print(x)
