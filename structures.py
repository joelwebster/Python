# CLASS
class Person(object):
    per_counter = 0  # class variable

    def __init__(self, name, age):  # constructor
        self.name = name  # instance variable
        self.age = age
        Person.per_counter += 1

        print "Calling parent constructor"

    def displayPerson(self):
        print "Name: ", self.name
        print "Age: ", self.age

    def displayCounter(self):
        print "Number of Person: ", getattr(self,'per_counter')


# SUBCLASS
class Employee(Person):
    emp_counter = 0  # class variable

    def __init__(self, name, age):
        super(Employee,self).__init__(name,age)
        Employee.emp_counter += 1

        print "Calling child constructor"

    def displayCounter(self):
        print "Number of Employee: ", getattr(self,'emp_counter')

# INSTANCE OF CLASS
p = Person("Joel",25)
p2 = Person("James",40)
p.displayPerson()

e = Employee("Mike",24)
e2 = Employee("Dan",34)
e.displayPerson()

# number of persons
p.displayCounter()

# number of employees
e.displayCounter()

