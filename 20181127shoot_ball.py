# shoot ball with computer


import random


def hm_shoot(l, _hm_shoot):
    """射门角度， 玩家射门位置"""
    _pc_guess = random.choice(l)
    print('电脑防守位置：{}'.format(_pc_guess))  ####
    if _pc_guess == _hm_shoot:
        return 1
    else:
        return 0


def pc_shoot(l, _hm_guess):
    """射门角度， PC射门位置"""
    _pc_shoot = random.choice(l)
    print('电脑射门位置：{}'.format(_pc_shoot))  ####
    if _pc_shoot == _hm_guess:
        return 1
    else:
        return 0


l = ['左', '中', '右']
# l = ['右']
_pc_score, _hm_score = 0, 0
for i in range(9):
    _hm_shoot = input('\n玩家第{}球，射门位置：'.format(i+1))
    game_hm = hm_shoot(l, _hm_shoot)
    if game_hm == 0:
        print('Goal!')
        _hm_score += 1
        print('玩家得分+1')

    _hm_guess = input('\n电脑第{}球，防守位置：'.format(i+1))
    game_pc = pc_shoot(l, _hm_guess)
    if game_pc == 0:
        print('Goal!')
        _pc_score += 1
        print('电脑得分+1')

    if i < 4 and (_hm_score >= _pc_score + (5 - i) or _pc_score >= _hm_score + (5 - i)):
        print('提前结束比赛！')
        break

    if _hm_score < 5 and _pc_score < 5:
        continue
    elif _pc_score == _hm_score:
        continue
    else:
        break


print('玩家射门得分：{}'.format(_hm_score))
print('电脑射门得分：{}'.format(_pc_score))
