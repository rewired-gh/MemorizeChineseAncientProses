# coding=utf-8
import numpy.random as ran

# 运行参数：
slow = 50  # 挖空时*最少*挖去的文字个数
shigh = 51 + 1  # 挖空时*最多*挖去的文字个数 + 1
clow = 1  # *最少*的连续文字个数
chigh = 2 + 1  # *最多*的连续文字个数 + 1
phlow = 1  # *最少*用几个占位符代替一个字
phhigh = 1 + 1  # *最多*用几个占位符代替一个字 + 1
placeholder = '＿'  # 代替被挖空的文字的字符
puncs = set([',', '.', '?', ':', ';', '!', '-', '"', "'", '，', '。', '？', '、',
             '！', '：', '；', '“', '”', '‘', '’', '(', ')', '—', '《', '》', '*', '\n'])  # 标点符号和换行符号
spaces = set(['　', ' '])  # 冗余的空格

skp = 0
ctn = ran.randint(clow, chigh)
roast = ''
with open("input.txt", mode='r', encoding='utf-8') as rawfile:
    raw = rawfile.read()
for char in raw:
    if char in spaces:
        continue
    if char in puncs:
        roast = roast + char
    elif skp == 0:
        ctn -= 1
        roast = roast + char
        if ctn == 0:
            skp = ran.randint(slow, shigh)
    elif ctn == 0:
        skp -= 1
        ph = ran.randint(phlow, phhigh)
        while ph > 0:
            roast = roast + placeholder
            ph -= 1
        if skp == 0:
            ctn = ran.randint(clow, chigh)
print(roast)
with open("output.txt", mode='w', encoding='utf-8') as roastfile:
    roastfile.write(roast)
