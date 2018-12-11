# 返回首字母大写 以.结尾的字符串

def correct_sentence(text: str) -> str:
    a = list(text)
    print(list(text))
    print(a.extend('.'))
    return text.capitalize() if text[-1]=='.'else ''.join(list(text).append('.'))


a = correct_sentence('greetings, friend')
print(a)