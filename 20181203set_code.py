def set_code(code_right:str, turn_num:int):
    code_turnning = list(code_right)
    for i in range(0, len(code_turnning)):
        if code_turnning[i] != ' ':
            if turn_num >= 0:
                if ord(code_turnning[i])+turn_num <= 122:
                    code_turnning[i] = chr(ord(code_turnning[i])+turn_num)
                else:
                    code_turnning[i] = chr(96 + ord(code_turnning[i])+turn_num - 122)
            else:
                code_turnning[i] = chr(ord(code_turnning[i])+26+turn_num)
    return ''.join(code_turnning)

s = 'a b c'
print('state secret')
a = set_code("state secret", -13)
print(a)
print('iycfbu junj')

print(ord('_'))
