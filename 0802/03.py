'''
decorator define
'''
def log(func):
    def wrapper(*args,**kw):
        print 'call %s():'%func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now():
    print '2015-3-25'

now()
print now.__name__#wrapper






'''
decorator define with args
'''
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print '2015-3-25'

now()
print now.__name__#wrapper



'''
functools 
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s()'%func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now():
    print '2015-3-25'

now()
print now.__name__#now

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('josn')
def now():
    print '2013-14'

now()
print now.__name__

