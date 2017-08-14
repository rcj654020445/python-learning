'''
sorted()函数是一个高阶函数，他接收一个key函数来实现自定义的排序
'''
l = ['bob', 'about', 'Zoo', 'Credit'];
print(sorted(l,key=str.lower))
print(sorted(l,key=str.lower,reverse=True))


from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=itemgetter(0)))
print(sorted(L,key=lambda t:t[1]))
print(sorted(L,key=itemgetter(1),reverse=True))


