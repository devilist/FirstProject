#! /usr/bin/env python3

# 函数


def make_a_sound():
	print("quack")


make_a_sound()


def agree():
	return True


if agree():
	print("ok!")
else:
	print("not ok")


def echo(anything):
	return anything + ' ' + anything


print(echo("日你妈哟!"))


def commentary(color):
	if color == 'red':
		return "It's a tomato."
	elif color == "green":
		return "It's a green pepper."
	elif color == 'bee purple':
		return "I don't know what it is, but only bees can see it."
	else:
		return "I've never heard of the color " + color + "."


comment = commentary('blue')
print(comment)


# 位置参数
def menu(wine, entree, dessert):
	return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))

# 关键字参数
menu(entree='dzczc', dessert="dsdd", wine="ieriue")


# 使用*收集位置参数
def print_args(*args):
	print('Positional argument tuple:', args)


print_args(1, 2, 4, 'afaf', 'assafs')


def print_more(required1, required2, *args):
	print('Need this one:', required1)
	print('Need this one too:', required2)
	print('All the rest:', args)


print_more('q', 's', 'w', 'a')


# 使用**收集关键字参数
def print_kwargs(**kwargs):
	print('Keyword arguments:', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


def add_args(arg1, arg2):
	print(arg1 + arg2)


print(type(add_args))


def run_something_with_args(func, args1, args2):
	func(args1, args2)


run_something_with_args(add_args, 2, 8)


def sum_args(*args):
	print(sum(args))


def run_with_positional_args(func, *args):
	return func(*args)


run_with_positional_args(sum_args, 1, 2, 3, 4)


# 内部函数

def knights(saying):
	def inner(quote):
		return "We are the knights who say: '%s'" % quote

	return inner(saying)


print(knights('afafjferewfndm,sd,dsfsdgll'))


# 闭包
# 内部函数可以看作一个闭包。闭包是一个可以由另一个函数动态生成的函数，
# 并且可以改变和存储函数外创建的变量的值。

# 定义函数knights2:
# inner2() 直接使用外部的saying 参数，而不是通过另外一个参数获取。
# knights2() 返回值为inner2 函数，而不是调用它。
#
# inner2() 函数可以得到saying 参数的值并且记录下来。
# return inner2 这一行返回的是inner2 函数的复制（没有直接调用）。
# 所以它就是一个闭包：一个被动态创建的可以记录外部变量的函数。

def knights2(saying):
	def inner2():
		return "We are the knights who say: '%s'" % saying

	return inner2


a = knights2("duck")
b = knights2("Hasenpfeffer")

print(type(a))
print(type(b))
print(a())
print(b())


# 匿名函数：lambda()函数
def edit_story(words, func):
	for word in words:
		print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']
edit_story(stairs, lambda word: word.capitalize() + '!')
