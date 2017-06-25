#! /usr/bin/env python3

# 生成器
# 用来创建Python 序列的一个对象。
# 使用它可以迭代庞大的序列，且不需要在内存中创建和存储整个序列。
# 通常，生成器是为迭代器产生数据的


# 生成器函数
# 生成器函数和普通函数类似，但是它的返回值使用yield 语句声明而不是return
def my_range(first=0, last=10, step=1):
	number = first
	while number < last:
		yield number
		number += step


ranger = my_range(1, 5, 3)

for x in ranger:
	print(x)


# 装饰器
# 有时你需要在不改变源代码的情况下修改已经存在的函数。常见的例子是增加一句调试声明，以查看传入的参数。

# 装饰器实质上是一个函数。它把一个函数作为输入并且返回另外一个函数。

# 在装饰器中，通常使用下面这些Python 技巧：
# • *args 和**kwargs
# • 闭包
# • 作为参数的函数

# 函数document_it() 定义了一个装饰器，会实现如下功能：
# • 打印输出函数的名字和参数的值
# • 执行含有参数的函数
# • 打印输出结果
# • 返回修改后的函数
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result

	return new_function


def square_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result * result

	return new_function


@square_it
@document_it
def add_ints(a, b):
	return a + b


# cooler_add_ints = document_it(add_ints)
# print(cooler_add_ints(3, 6))

add_ints(56, 68)
