#! /usr/bin/env python3

from pprint import pprint

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))

f_out = open('relativity', 'wt')
# f_out.write(poem)
print(poem, file=f_out)
f_out.close()

f_in = open('relativity', 'rt')
poem_1 = f_in.read()
f_in.close()
print(poem_1)
poem_2 = ''
f_in_2 = open('relativity', 'rt')
for line in f_in_2:
	poem_2 += line
f_in_2.close()
print(poem_2)

import csv
import os

print(os.path.exists('financius.csv'))
print(os.path.isfile('financius.csv'))

with open('financius.csv', 'rt') as f_in_3:
	csv_in = csv.reader(f_in_3)
	csv_in_1 = csv.DictReader(f_in_3, fieldnames=['date', 'time', '3', '4', '5', '6', '7', '8', '9', '0', '11', '12'])
	financius = [row for row in csv_in]
	financius_1 = [row for row in csv_in_1]

print(financius)
print(financius_1)
