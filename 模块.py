#! /usr/bin/env python3

import sys
# import 数据类型

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')
print(dir())
