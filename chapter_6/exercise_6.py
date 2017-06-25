#! /usr/bin/env python3


class Bill():
	def __init__(self, description):
		self.description = description


class Tail():
	def __init__(self, length):
		self.length = length


class Duck:
	"""
	鸭子
	"""

	def __init__(self, input_bill, input_tail):
		"""
		初始化
		:param input_bill:
		:param input_tail:
		"""
		self.bill = input_bill
		self.tail = input_tail

	def about(self):
		print('this Duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')


bill = Bill('orange')
tail = Tail('long')

duck = Duck(bill, tail)

duck.about()

# 命名元组
from collections import namedtuple

TupleDuck = namedtuple('TupleDuck', 'bill tail')
tupleDuck = TupleDuck('orange', 'long')
print(tupleDuck)
print(tupleDuck.bill)
print(tupleDuck.tail)


class Thing:
	pass


example = Thing()
print(Thing)
print(example)


class Thing2:
	def __init__(self, letters):
		self.letters = letters


Thing2.letters = 'abc'
example2 = Thing2('abc')
print(Thing2.letters)
print(example2.letters)


class Element:
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

	def dump(self):
		print('name:', self.name, 'symbol:', self.symbol, 'number:', self.number)

	def __str__(self):
		return 'name: ' + self.name + ' symbol: ' + self.symbol + ' number: ' + str(self.number)


dict_element = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

element = Element(dict_element.get('name'), dict_element.get('symbol'), dict_element.get('number'))
element.dump()
print(element)


class Element1:
	def __init__(self, name, symbol, number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, input_name):
		self.__name = input_name

	@property
	def symbol(self):
		return self.__symbol

	@symbol.setter
	def symbol(self, input_symbol):
		self.__symbol = input_symbol

	@property
	def number(self):
		return self.__number

	@name.setter
	def number(self, input_number):
		self.__number = input_number

	def dump(self):
		print('name:', self.name, 'symbol:', self.symbol, 'number:', self.number)

	def __str__(self):
		return 'name: ' + self.name + ' symbol: ' + self.symbol + ' number: ' + str(self.number)

element1 = Element(dict_element.get('name'), dict_element.get('symbol'), dict_element.get('number'))

print(element1.name)
print(element1.symbol)
print(element1.number)
print(element1)
