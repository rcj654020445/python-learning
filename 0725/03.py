'''
filter
    parama1 函数名
    parama2 可迭代的对象
    return  迭代器
'''
def is_odd(n):
	return n%2==1
print(list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])))