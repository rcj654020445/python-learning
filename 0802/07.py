#Mixin
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass


class Parrot(Bird):
    pass

class RunnableMixin(object):
    def run(self):
        print 'runing'

class FlyableMixin(object):
    def fly(self):
        print 'flying'

class Dog(Mammal,RunnableMixin):
    pass

class Parrot(Bird,FlyableMixin):
    pass
