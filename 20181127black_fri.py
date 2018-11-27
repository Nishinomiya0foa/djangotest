# 找寻任意年份中的黑色星期五

import calendar

def get_black_fri_of_a_year(y):
    l = []
    for i in range(1, 12):
        x = calendar.weekday(y, i, 13)  # 返回 y-m-d 是星期几
        if x == 4:
            l.append('{}-{}-13'.format(y, i))
    return l

x = get_black_fri_of_a_year(2046)
for i in x:
    print(i)
