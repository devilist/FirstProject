#! /usr/bin/env python3
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串
print(counter)
print(miles)
print(name)

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

print(8 / 3)
print(8 // 3)

str = 'Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串
print('Ru\noob')
print(r'Ru\noob')
print(str[0], str[5])
print(str[-1], str[-6])

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
print('\n')

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print('\n')

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
	print('Rose 在集合中')
else:
	print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
print('\n')

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print('keys are: ', tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print({x: x**2 for x in (2, 4, 6)})
print('\n')

print("我叫 %s 今年 %d 岁!" % ('小明', 10))

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)




