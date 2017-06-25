#! /usr/bin/env python3

# 使用setdefault()和 defaultdict() 处理缺失的键
import pprint
from collections import OrderedDict

periodic_table = {'Hydrogen': 1, 'Helium': 2}

# 如果键不在字典中，新的默认值会被添加进去
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

# 如果试图把一个不同的默认值赋给已经存在的键，不会改变原来的值，仍将返回初始值：
helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

from collections import defaultdict

periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']

print(periodic_table['Lead'])
print(periodic_table)

# 使用Counter()计数
from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(dict(breakfast_counter))

# 函数most_common() 以降序返回所有元素，或者如果给定一个数字，会返回该数字前的的元素
breakfast_counter.most_common()
print(breakfast_counter)
print(breakfast_counter.most_common(1))

quotes = OrderedDict([
	('Moe', 'A wise guy, huh?'),
	('Larry', 'Ow!'),
	('Curly', 'Nyuk nyuk!'),
	])
pprint.pprint(quotes)


