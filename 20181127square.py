# 创建一个n宫格。 长宽为n
# 将 1 - n² 的数 放入这n²个格子
# 每横竖斜 的和都相等



def square(n):
    for i in range(n):
        for j in range(n):
            print('*', end='')

x = square(3)