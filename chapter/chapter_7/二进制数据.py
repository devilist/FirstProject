#! /usr/bin/env python3
from pprint import pprint

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)  # bytes 类型不可变
the_bytes_array = bytearray(blist)  # bytearray 类型可变
print(the_bytes)
print(the_bytes_array)
the_bytes_array[1] = 129
print(the_bytes_array)

the_bytes_1 = bytes(range(0, 256))
pprint(the_bytes_1)



import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
	b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
	width, height = struct.unpack('>LL', data[16:24])
	print('Valid PNG, width', width, 'height', height)
else:
	print('Not a valid PNG')
