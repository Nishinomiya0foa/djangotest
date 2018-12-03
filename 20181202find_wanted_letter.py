def get_wanted_letter(words):
    """找到字符串中出现最多的字符"""
    b = []
    for a in words:
        if not a.isalpha():
            continue
        b.append(a.lower())
    s = {}
    for i in range(0, len(b)):
        s.setdefault(b[i], b.count(b[i]))
    m = {}
    for key, value in s.items():
        if value == max(s.values()):
            m.setdefault(key.lower(), value)
    return min(m.keys())


a = get_wanted_letter('Gregor then turned to look out the window at the dull weather.Nooooooooooo!!! Why!?!')
print(a)


