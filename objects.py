class Car:
    carCount = 0

    def __init__(self,manufacturer,model):
        self.manufacturer = manufacturer
        self.model = model
        Car.carCount +=1

    def __str__( self ):
        return self.manufacturer + " " + self.model

    @staticmethod
    def display_count():
        print "Total number of cars: ",Car.carCount

    def display_car(self):
        print "Manufacturer: ", self.manufacturer
        print "Model: ", self.model
        print "\n"


# subclass
class SUV(Car,object):
    def __init__(self,manufacturer,model):
        super(SUV, self).__init__(manufacturer, model)

        print "Calling child constructor"

    def child_method(self):
        print "Calling child method"

car1 = Car("Ford","Fiesta")
car2 = Car("Vauxhall","Nova")
car3 = Car("Fiat","500")

car1.display_count()
car2.display_car()

print getattr(car1,'model')
setattr(car1,'model',"Focus")
print getattr(car1,'model')

print hasattr(car2,'manufacturer')
print hasattr(car1,'age')


# create SUV object
s = SUV("Renault","Clio") # instance of SUV subclass
print s.__str__()


list = [car1,car2]
list.append(car3)

for l in list:
    print l