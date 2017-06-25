#! /usr/bin/env python3

guess_me = 7
start0 = 1
while True:
	if start0 < guess_me:
		print("low")
		start0 += 1
	elif start0 == guess_me:
		print('yeh')
		break

for item in [1, 2, 3, 4]:
	print(item)
num_list = [num for num in range(0, 9) if num % 2 == 0]
print(num_list)
num_dict = {num: num ** 2 for num in range(0, 6)}
print(num_dict)
odd = {num for num in range(0, 9) if num % 2 == 1}
print(odd)

x0 = (item for item in ('got ', 1))
for item in x0:
	print(item)


def start_end_flag(func):
	def new_func():
		print('start: ', func.__name__)
		result = func()
		print(result)
		print('end: ', func.__name__)
		return result

	return new_func


@start_end_flag
def good():
	return ['a', 'b', 'c']


good_list = good()
print(good_list)


def get_goods(first=1, end=10, step=2):
	num = first
	while num < end:
		yield num
		num += step


for x in get_goods():
	print(x)


class OopsException(Exception):
	print('Caught an oops')


try:
	raise OopsException
except OopsException as x:
	print(x)

tittles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(tittles, plots))
print(movies)
