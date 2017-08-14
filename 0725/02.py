'''
map()函数
     接收两个参数，
     一个是函数，一个是Iterable，
     map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''

def f(x):
	return x*x;
'''
结果r是一个Iterator
'''
r=map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

while True:
	try:
		x=next(r)
	except StopIteration:
		break
	


'''
reduce()函数
reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
from functools import reduce
def add(x,y):
	return x+y;

print(reduce(add,[1, 3, 5, 7, 9]))

'''
例子2：

'''
def str2int(s):
	def fn(x,y):
		return x*10+y;
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))

print(str2int('13579'))