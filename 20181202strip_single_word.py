def strip_single_word(word_list: list):
    """去除word_list（数组，纯数字组成）里的单独出现的数字"""
    d = {}
    c = []
    for i in word_list:
        a = 1
        d.setdefault(i, 0)
        d[i] = d[i]+1
    for key, value in d.items():
        if value == 1:
            c.append(key)
            word_list.remove(key)
    return word_list


d = [1, 2, 4, 3, 4, 4, 2, 0, 3]
c = strip_single_word(d)
