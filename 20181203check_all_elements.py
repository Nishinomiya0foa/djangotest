def check_all_elements(words:list):
    """check_all_elements, return True if they are all the same"""
    for i in range(0, len(words)):
        if words[i] == words[0]:
            pass
        else:
            return False
    return True

xx = check_all_elements(['', ''])
print(xx)