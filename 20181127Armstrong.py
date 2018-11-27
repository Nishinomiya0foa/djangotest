# 找阿姆斯特朗数
# 正整数 = 各位数字的立方和

def Armstrong(num):
    num2str = str(num)
    l = []
    for i in num2str:
        l.append(int(i)**3)
    sun = 0
    for i in range(0, len(l)):
        sun += l[i]
    if num == sun:
        return True

if __name__ == '__main__':
    for n in range(0, 1000):
        if Armstrong(n):
            print('{}是Armstrong数'.format(n))
