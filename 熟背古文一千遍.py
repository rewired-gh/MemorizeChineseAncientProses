# coding=utf-8
import numpy.random as ran

# 运行参数：
low = 2  # 挖空时*最少*挖去的文字个数
high = 4+1  # 挖空时*最多*挖去的文字个数 + 1
placeholder = '＿'  # 代替被挖空的文字的字符
puncs = set([',', '.', '?', ':', ';', '!', '-', '"', "'", '，', '。', '？',
             '！', '：', '；', '“', '”', '‘', '’', '(', ')', '—', '\n'])  # 标点符号和换行符号
spaces = set(['　', ' '])  # 冗余的空格

csp = 0
roast = ''
with open("input.txt", mode='r', encoding='utf-8') as rawfile:
    raw = rawfile.read()
for char in raw:
    if char in spaces:
        continue
    if char in puncs:
        roast = roast + char
    elif csp == 0:
        csp = ran.randint(low, high)
        roast = roast + char
    else:
        csp -= 1
        roast = roast + placeholder
print(roast)
with open("output.txt", mode='w', encoding='utf-8') as roastfile:
    roastfile.write(roast)
