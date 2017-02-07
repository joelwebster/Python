# parent class
class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def noise(self):
        print "PERSON NOISE"

# child subclass
class Student(Person):
    def __init__(self, age, height, weight, school):
        super(Student,self).__init__("Student", age, height, weight)
        self.school = school

    def noise(self):
        print "STUDENT NOISE"

# child subclass
class Teacher(Person):
    def __init__(self,name,age,height,weight,salary):
        Person.__init__(self,name,age,height,weight)
        self.salary = salary

    def noise(self):
        print "TEACHER NOISE"


# create person obj
p = Person('John',43,201,96)

# create student obj
s = Student(25,178,90,'SE')

# create teacher obj
t = Teacher('Julie',31,166,70,26000)

# print person obj
print getattr(p,'name')

# replacement characters
print "%s %s %s" % (p.name, p.age, p.height)

# print student child data
print "%s %s" % (s.name,s.school)

# print teacher child data
print "%s has a salary of %dGBP" % (t.name,t.salary)

# instance of?
print isinstance(p,Person)
print isinstance(s,Person)
print isinstance(t,Person)
print isinstance(t,Teacher)
print isinstance(s,Teacher)

# test method overloading
t.noise()
s.noise()
p.noise()
