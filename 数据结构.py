#! /usr/bin/env python3


matrix = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])
print([row[0] for row in matrix])
print([row[1] for row in matrix])
print([row[2] for row in matrix])
print([row[3] for row in matrix])

a = set("'ssds','wrt'")
print(a)

tel = {'jack': 4098, 'sape': 4139}
print(tel)
print(tel.keys())
print(tel.values())

z = dict(sap=4139, guio=4127, jak=4098)
print(z.items())
print(z)