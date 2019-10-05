#! /usr/bin/env python3

# 列表
year_list = [1987, 1988, 1989, 1990, 1991]
things = ['mozzarella', 'cinderella', 'salmonella', 'Groucho', 'Chico', 'Harpo', 'Zeppo']

for item in things:
	print(item.capitalize())
	print(item.upper())

print(things[1], things[-1])
things[3] = 'zuoaisfs'
print(things)
print(things[::-2])

things.remove('Chico')
print(things)
del things[-1]
print(things)
print(things.pop())
print(things)
print(things.pop(0))
print(things)
print(things.pop(1))
print(things)
print(things.index('cinderella'))
print('sa' in things)
print(things.count('as'))
print(' @ '.join(things))

thing = ['mozzarella', 'cinderella', 'salmonella', 'Groucho', 'Chico', 'Harpo', 'Zeppo']
thing.sort(reverse=True)
print(thing)
thing0 = thing
thing0[0] = '1'
print(thing)
print(thing0)
thing1 = thing0.copy()
thing2 = list(thing0)
thing3 = thing0[:]
thing0[0] = '12'
print(thing0)
print(thing1)
print(thing2)
print(thing3)

python = 'python'
python = python[::-1]
print(python)

# 元组
t_tuple = ('a', 1, 3)
print(t_tuple)
x, y, z = t_tuple
print(x, y, z)
print(tuple(thing0))

# 字典
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)
print(e2f.get('walrus'))
print(list(e2f.keys()))
print(e2f.items())

anim = {'cats': 12, 'octopi': 23, 'emus': 34}
cat_list = ['Henri', 'Grumpy']
lef = {'animals': anim, 'cat': cat_list}
print(lef)
