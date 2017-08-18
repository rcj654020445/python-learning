###__slots_
class Student(object):
    __slots__ = ('name','age');

class GraduateStudent(Student):
    __slots__ = ('score');

g = GraduateStudent();
g.score = 75;
g.name = 'Joje';
g.age = 18;
#g.grade = 'san nian ji';
