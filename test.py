import re

line = "Cats are smarter 3than Dogs"

matchObj = re.match(r'^Cats', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'\bmar', line, re.M)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")


key2 = '1'
key = '321_32@qq.com'
email = ['3218373@qq.cin', 'fewfw21121', '2132132@qq.com']

for i in email:
    matchObj = re.match(r'(\S)*(@\b)(\S)*(\.com$)', i)
    if matchObj:
        print(matchObj.group(), '是邮箱地址')
    else:
        print("NO")


num = '140-1244-5232'
matchObj = re.match(r'1(\d){2}-(\d){4}-(\d){4}\b', num)
num2 = '140 - 1244 - 5232'
splitObj2 = re.split(r'[\s+]', num2)
print(splitObj2)
print(''.join(splitObj2))
matchObj2 = re.match(r'1(\d){2}([ ])-([ ])(\d){4}([ ])-([ ])(\d){4}\b', num2)

if matchObj:
    print(matchObj.group())
if matchObj2:
    print("222:", matchObj2.group())


# 匹配由单个空格组成的任意单词对
name1 = 'fds fef'
matchObj = re.match(r'^[a-z]+ [a-z]+$', name1)
if matchObj:
    print('匹配由单个空格组成的任意单词对:', matchObj.group())
else:
    print("no match")

# 匹配简单网址
url = 'www.goo124_gle.com/'
matchObj = re.match(r'(^www\.)?(\w+)(\.com)(\/$)+', url)
if matchObj:
    print("是网址：", matchObj.group())
    print("是网址：", matchObj.group(4))

#
l = 'xbaxbax'
matchObj = re.match(r'(^ba)*(ba)?(^ba)*', l)
if matchObj:
    print('字符串 {} 中\'ba\'出现仅1次'.format(l))

# 匹配b[aoieu]t单词
word = 'but'
matchObj = re.match(r'b[aoieu]t', word)
if matchObj:
    print('匹配的单词为：', matchObj.group())

# 匹配AccBrian
word = 'AccBrian'
matchObj = re.match(r'AccBrian', word)
if matchObj:
    print('匹配的单词为：', matchObj.group())

# search方法与match的不同
word = 'AccBrian'
matchObj = re.search(r'cB', word)
if matchObj:
    print('search方法可从{}中匹配到{}'.format(word, matchObj.group()))
else:
    print('search方法不可从{}中匹配到{}'.format(word, 'cB'))
matchObj2 = re.match(r'cB', word)
if matchObj2:
    print('match方法可从{}中匹配到{}'.format(word, matchObj2.group()))
else:
    print('match方法不可从{}中匹配到{}'.format(word, 'cB'))

# findall方法
l = 'this this thibbb fdjthis'
matchObj = re.findall(r'thi', l)
if matchObj:
    print(matchObj)

# ?扩展符
pra = '''
    The first line
    the second line
    the third line
'''
matchObj = re.findall(r'th.+', pra)
matchObj2 = re.findall(r'(?s)th.+', pra)
if matchObj:
    print(matchObj)
if matchObj2:
    print(matchObj2)

# 匹配12个月
month = '2'
matchObj = re.match(r'1[0-2]|0?[0-9]', month)
if matchObj:
    print(matchObj.group())


#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

for i in range(randrange(5, 11)):
    dtint = randrange(542421512)	# pick date
    dtstr = ctime(dtint)	# date string
    llen = randrange(4, 7)	# login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)	# domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    with open('C:\\Users\Administrator\Desktop\\redata.txt', 'a+', encoding='utf-8') as fr:
        fr.write('%s::%s@%s.%s::%d-%d-%d\n' %
                 (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
    # print('%s::%s@%s.%s::%d-%d-%d' %
    #              (dtstr, login, dom, choice(tlds), dtint, llen, dlen))

# 判断1111.txt中一周的每一天出现的次数
with open('C:\\Users\Administrator\Desktop\\redata.txt', 'r', encoding='utf-8') as f:
    everyLine = f.readlines()
    # mon, tue, wed, thu, fri, sat, son = 0
    l = [0, 0, 0, 0, 0, 0, 0]
    for line in everyLine:
        matchObj = re.match(r'(?i)^mon|tue|wed|thu|fri|sat|sun', line)
        if matchObj.group() == 'Mon':
            l[0] += 1
        elif matchObj.group() == 'Tue':
            l[1] += 1
        elif matchObj.group() == 'Wed':
            l[2] += 1
        elif matchObj.group() == 'Thu':
            l[3] += 1
        elif matchObj.group() == 'Fri':
            l[4] += 1
        elif matchObj.group() == 'Sat':
            l[5] += 1
        elif matchObj.group() == 'Sun':
            l[6] += 1
    for i in range(0, 7):
        print("星期{}出现了{}次".format(i+1, l[i]))
    # 提取年份
    # for line2 in everyLine:
    #     matchObj2 = re.search(r'(19\d+)', line2)
    #     print(matchObj2.group(1))
    # 提取完整的时间戳
    for line3 in everyLine:
        # 完整时间戳
        matchObj3 = re.search(r'(.|\n)*(19)(\d+)+', line3)
        # 仅月份
        matchObj5 = re.search(r'(\s)[A-Za-z]+(\s)', matchObj3.group())
        # 仅年份
        matchObj6 = re.search(r'(\s)\d\d\d\d', matchObj3.group())
        # 仅时间
        matchObj7 = re.search(r'\d+:\d+:\d+', matchObj3.group())
        # 邮箱
        matchObj4 = re.search(r'(::.*[a-z])', line3)
        mail_all = matchObj4.group()[2:]
        # 邮箱@前的字段
        matchObj_first_name = re.match(r'[a-z]+', mail_all)
        # 邮箱@后的字段
        matchObj_second_name = re.search(r'@([a-z]+)\.', mail_all)
        # 邮箱最后一段
        matchObj_third_name = re.search(r'\.([a-z]+)', mail_all)
        # print(mail_all, matchObj_first_name.group(), matchObj_second_name.group(1), matchObj_third_name.group(1))
        # 用我的邮箱代替这些邮箱部分
        my_mail = re.sub(mail_all, 'mxstarbucks@sina.com', mail_all)

        # print(matchObj3.group()[:24], '   ', matchObj4.group()[2:], matchObj5.group(), matchObj6.group(), matchObj7.group())



# 匹配固话 区号（0512-）可选
number = '(0512)67231352'
matchObj_num = re.match(r'((\d\d\d\d-)|(\(\d\d\d\d\)))?(\d)+', number)
print(len(matchObj_num.group()))
if len(matchObj_num.group()) == 8 or len(matchObj_num.group()) == 13 or len(matchObj_num.group()) == 14:
    print("{}是固话。".format(number))

