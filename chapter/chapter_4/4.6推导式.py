#! /usr/bin/env python3


# 列表推导式
# [expression for item in iterable if condition]

a_list = [number for number in range(1, 9) if number % 2 == 0]

print('\n 列表推导式')
print('[expression for item in iterable if condition] \n')
print('a_list = [number for number in range(1, 9) if number % 2 == 0]')
print('a_list is :', a_list)

rows = range(1, 5)
cols = range(1, 4)
cells = [(row, col) for row in rows for col in cols]

print('''
rows = range(1, 5)
cols = range(1, 4)
cells = [(row, col) for row in rows for col in cols]
''')
print('cells is : ', cells)
print('--------------------------------------------------')

# 字典推导式
# { key_expression : value_expression for expression in iterable }

word = 'letter'
letter_count = {letter: word.count(letter) for letter in set(word)}

print('\n 字典推导式')
print('{ key_expression : value_expression for expression in iterable }')
print('''
word = 'letter'
letter_count = {letter: word.count(letter) for letter in set(word)}''')
print('letter_count is: ', letter_count)
print('--------------------------------------------------')

# 集合推导式
# {expression for expression in iterable }

a_set = {number for number in range(1, 6) if number % 3 == 1}
print('\n 集合推导式')
print('{expression for expression in iterable }')
print('''
a_set = {number for number in range(1, 6) if number % 3 == 1}''')
print('a_set is: ', a_set)
print('--------------------------------------------------')
