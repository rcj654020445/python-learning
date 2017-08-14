print map(lambda x:x*x,[1, 2, 3, 4, 5, 6, 7, 8, 9])

#var = fun
f = lambda x:x*x
print f(5)

#lambda func as return
def f(x, y):
    return lambda :x * y

a = f(4,5)
print a  #<function <lambda> at 0x030FDDB0>
print a()#20