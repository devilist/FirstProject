#! /usr/bin/env python3

from pprint import pprint

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))
###############################################
# 写文件
f_out = open('relativity', 'wt')
# f_out.write(poem)
print(poem, file=f_out)
f_out.close()

f_out = open('a', 'wt')
print(poem, file=f_out, sep=' ', end=' ')
f_out.close()
###############################################
# 读文件
f_in = open('relativity', 'rt')
poem_1 = f_in.read()
f_in.close()
print('poem_1: 一次性全部读入')
print(poem_1)

poem_2 = ''
f_in_2 = open('relativity', 'rt')
for line in f_in_2:
    poem_2 += line
f_in_2.close()
print('poem_2:  迭代器方式')
print(poem_2)

import csv
import os

print(os.path.exists('financius.csv'))
print(os.path.isfile('financius.csv'))

with open('financius.csv', mode='rt', encoding='utf-8') as f_in_3:  # 上下文管理器
    csv_in = csv.reader(f_in_3)
    csv_in_1 = csv.DictReader(f_in_3, fieldnames=['date', 'time', 's3', 's4', 's5', 's6',
                                                  's7', 's8', 's9', 's0', 's11', 's12'])
    # 列表推导式
    financius = [row for row in csv_in]
    financius_1 = [row for row in csv_in_1]

print('csv.reader:')
print(financius)
print('csv.DictReader')
print(financius_1)
