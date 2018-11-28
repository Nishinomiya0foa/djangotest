# 田忌赛马

def race(qiwang,tianji):
    _race = {}
    _race[qiwang[0]] = tianji[1]
    _race[qiwang[1]] = tianji[2]
    _race[qiwang[2]] = tianji[0]
    return _race

qiwang = [3, 6, 9]
tianji = [2, 5, 8]
print(race(qiwang, tianji))