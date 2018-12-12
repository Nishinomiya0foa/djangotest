import re


def correct_sentence(text: str) -> str:
    """返回首字母大写 以.结尾的字符串"""
    a = list(text)
    a[0] = a[0].upper()
    if a[-1] != '.':
        a.append('.')
    return ''.join(a)


def first_word(text:str) -> str:
    """返回字符串的第一个单词"""
    _first_word = re.search(r'[A-Za-z]+\'?[a-z]?', text)
    return _first_word.group()

def second_index(text: str, symbol: str) -> [int, None]:
    """返回symbol第二次出现在text中的位置"""
    a = text
    l = []
    for i in range(0, len(a)):
        if symbol == a[i]:
            l.append(i)
    return l[1] if len(l) > 1 else None


def between_markers(text:str, signal1:str, signal2:str) -> [str,None]:
    """返回signal标记之间的字符串。"""
    target_str = []
    if signal1 in text and signal2 in text:
        for i in range(0,len(text)):
            if signal1[-1] == text[i] or signal2[0] == text[i]:
                target_str.append(i)
        try:
            return text[target_str[0]+1:target_str[1]]
        except IndexError as e:
            return ''
    elif signal2 or signal2 not in text:
        if signal1 not in text and signal2 not in text:
            return text
        elif signal2 not in text:
            return text[-1]
        elif signal1 not in text:
            return text[0]


if __name__ == '__main__':
    a = between_markers("<head><title>My new site</title></head>","<title>","</title>")
    print(a)




