class test(object):
    __slots__ = ('name', 'age', 'sex')

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __len__(self):
        return 4;

print test('Miclde')
a = test('Miclde');
print a;




class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def next(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 1000:
            raise StopIteration();
        return self.a

    def __getitem__(self, item):
        if isinstance(item,int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            L = []
            a, b = 1, 1
            start =item.start
            stop = item.stop
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b=b,a+b
            return L




for x in Fib():
    print  x

x = Fib();
print  x[8]
print  x[8:9]




class Chain(object):
    def __init__(self,path=''):
        self._path = path;

    def __getattr__(self, item):
        if item=='user':
            return lambda username: Chain('%s/user/%s' % (self._path, username))
        else:
            return Chain('%s/%s' % (self._path, item))


    def __str__(self):
        return  self._path;

#print  Chain().status.user
print  Chain().user('Jack')