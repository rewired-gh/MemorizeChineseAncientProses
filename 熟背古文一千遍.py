# coding=utf-8
import numpy.random as ran


# 运行参数：
最少跳过数 = 50  # 挖空时*最少*挖去的文字个数
最多跳过数 = 50 + 1  # 挖空时*最多*挖去的文字个数 + 1
最少保留数 = 1  # *最少*的连续文字个数
最多保留数 = 1 + 1  # *最多*的连续文字个数 + 1
最少替换数 = 1  # *最少*用几个占位符代替一个字
最多替换数 = 2 + 1  # *最多*用几个占位符代替一个字 + 1
占位符 = '＿'  # 代替被挖空的文字的字符
标点符号 = set([',', '.', '?', ':', ';', '!', '-', '"', "'", '，', '。', '？', '、', '！',
            '：', '；', '“', '”', '‘', '’', '(', ')', '—', '《', '》', '*', '\n'])  # 标点符号和换行符号
空白符号 = set(['　', ' '])  # 冗余的空白符号


# 高级自定义处理参数
高级模式开关 = True
advanced_flag_1 = False


# 自定义处理常量
keywords = set(['#', '['])


def power_proc(c):
    # 自定义处理逻辑（默认示例是弱兼容 Markdown 语法的处理）
    global advanced_flag_1
    global roast
    res = c in keywords or advanced_flag_1
    if (res):
        if (c == '\n'):
            advanced_flag_1 = False
        elif (advanced_flag_1 == False):
            advanced_flag_1 = True
        roast = roast + c
    return res


# 初始化
skp = 0
kp = ran.randint(最少保留数, 最多保留数)
roast = ''


# 主处理逻辑
with open("input.txt", mode='r', encoding='utf-8') as rawfile:
    raw = rawfile.read()

for char in raw:

    # 判断是否进行自定义处理，以及是否跳过其他处理
    if (power_proc(char)):
        continue

    # 略过空白字符
    if char in 空白符号:
        continue

    # 保留标点符号
    if char in 标点符号:
        roast = roast + char

    # 处于“保留”处理阶段时执行的逻辑
    elif skp == 0:
        kp -= 1
        roast = roast + char
        if kp == 0:
            skp = ran.randint(最少跳过数, 最多跳过数)

    # 处于“跳过”处理阶段时执行的逻辑
    elif kp == 0:
        skp -= 1
        rplc = ran.randint(最少替换数, 最多替换数)
        while rplc > 0:
            roast = roast + 占位符
            rplc -= 1
        if skp == 0:
            kp = ran.randint(最少保留数, 最多保留数)

# print(roast)

# 写入文件
with open("output.txt", mode='w', encoding='utf-8') as roastfile:
    roastfile.write(roast)
