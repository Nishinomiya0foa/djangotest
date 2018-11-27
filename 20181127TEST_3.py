# 3道练习题

# 制作一个骰子游戏：假想有3个6面骰子，可以掷出3~18的数，其中3~10为小，11~18为大。
# 起始为100分，每掷一次之前先押注，可押大小或数字，可重复下注。
# 掷出结果后，押中大小，所押分数翻倍返还；押中数字，所押分数10倍返还。
# 增加电脑玩家，同你一起进行游戏。

import random


def roll():
    _roll_1 = random.randint(1, 6)
    _roll_2 = random.randint(1, 6)
    _roll_3 = random.randint(1, 6)
    # print('三个骰子分别为:{},{},{}'.format(_roll_1, _roll_2, _roll_3))
    return (_roll_1, _roll_2, _roll_3, _roll_1+_roll_2+_roll_3)


def big_or_small(_roll_point_all):
    if _roll_point_all <= 10:
        return '小'
    else:
        return '大'


def point_win_or_lose(_point_drop, _roll_point_all, _guess_point):
    if _roll_point_all == _guess_point:
        _point_drop = -10 * _point_drop
    return _point_drop

def point_big_or_small(_point_drop, _roll_big_or_small, _guess_point):
    if _guess_point == _roll_big_or_small:
        _point_drop = -2 * _point_drop
    return _point_drop


_point_all = 100
_game_type = int(input("输入1选择猜大小，2选择猜点数："))

# 猜大小
if _game_type == 1:
    while _point_all > 0 and _point_all < 500:
        _roll_point = roll()
        _roll_point_all = _roll_point[3]
        _roll_big_or_small = big_or_small(_roll_point_all)
        _point_drop = int(input('输入下注点数：'))
        _guess_point = input('输入所猜大小：')
        # win_point = point_win_or_lose(_point_drop, _roll_point_all, _guess_point)
        win_point_big_or_small = point_big_or_small(_point_drop, _roll_big_or_small, _guess_point)
        print('筛子大小：{},{},{}, {}点{}'.format(_roll_point[0], _roll_point[1], _roll_point[2],
                                            _roll_point_all, _roll_big_or_small))
        _point_all = _point_all - win_point_big_or_small
        print('当前点数：{}'.format(_point_all))

elif _game_type == 2:
    while _point_all > 0 and _point_all < 500:
        _roll_point = roll()
        _roll_point_all = _roll_point[3]
        _roll_big_or_small = big_or_small(_roll_point_all)
        _point_drop = int(input('输入下注点数：'))
        _guess_point = int(input('输入所猜点数：'))
        win_point = point_win_or_lose(_point_drop, _roll_point_all, _guess_point)
        print('筛子大小：{},{},{}, {}点{}'.format(_roll_point[0], _roll_point[1], _roll_point[2],
                                            _roll_point_all, _roll_big_or_small))
        _point_all = _point_all - win_point
        print('当前点数：{}'.format(_point_all))

else:
    print("无效输入。")



# # 读文件中的一段字。 判断其各个字符出现的字数，并按字数进行排序
# with open('C:\\Users\Administrator\Desktop\\111.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     l = []
#     for i in line:
#         if i != '\n' and i != ' ':
#             l.append(i)
#     l = sorted(l)
#     i = 0
#     n = 0
#     while i < len(l) -1:
#         if l[i] == l[i+1]:
#             n += 1
#             i += 1
#             continue
#         print(l[i], n+1)
#         n = 0
#         i+=1
#     print(l)
