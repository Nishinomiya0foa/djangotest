# 找到连续出现最多次数的单词的出现次数

def find_most_repeat_word(text:str):
    pass


if __name__ == '__main__':
    a = find_most_repeat_word('adfsffffsss')
    print(a)


l = 'eaabbbccccdddddc'
s = []
d = {}

list = list(l)
print(list)
n = 0
for i in list:
    if i not in s:
        n = 0
        s.append(i)
        d[i] = n+1
    else:
        d[i] = n+2
        n += 1
        continue
print(d)
