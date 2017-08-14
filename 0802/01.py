def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()#func 1
f1 = lazy_sum(1, 3, 5, 7, 9)
print f1
print f1()#func 2
print f==f1#False

#closure
def count():
    fs = []
    for x in range(1,4):
        def f():
            return x * x
        fs.append(f)
    return fs
f1, f2, f3 = count();
print f1()#9
print f2()#9
print f3()#9

