#! /usr/bin/env python3

import unicodedata

mystery = unicodedata.name('\U0001f4a9')
values = unicodedata.lookup(mystery)

print(mystery)
print(values)

# 编码为字节
pop_byte = mystery.encode('utf-8')

print(pop_byte)
print(len(pop_byte))

# 解码为字符串

pop_str = pop_byte.decode('utf-8')
print(pop_str)

strings = '''
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.

'''

print(strings % ('roast beef', 'ham', 'head', 'clam'))

letter = '''
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}

'''

response = {'salutation': 1,
			'name': 2,
			'product': 3,
			'verbed': 4,
			'room': 5,
			'animals': 6,
			'amount': 7,
			'percent': 8,
			'spokesman': 9,
			'job_title': 10}

print(letter.format(salutation=response.get('salutation'),
					name=response.get('name'),
					product=response.get('product'),
					verbed=response.get('verbed'),
					room=response.get('room'),
					animals=response.get('animals'),
					amount=response.get('amount'),
					percent=response.get('percent'),
					spokesman=response.get('spokesman'),
					job_title=response.get('job_title')))
