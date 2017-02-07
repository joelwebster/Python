class Car:
    carCount = 0

    def __init__(self,manufacturer,model):
        self.manufacturer = manufacturer
        self.model = model
        Car.carCount +=1

    def __str__( self ):
        return self.manufacturer + " " + self.model

    def displayCount(self):
        print "Total number of cars: ",Car.carCount, "\n"

    def displayCar(self):
        print "Manufacturer: ", self.manufacturer
        print "Model: ", self.model, "\n"


# subclass
class SUV(Car,object):
    def __init__(self,manufacturer,model):
        super(SUV, self).__init__(manufacturer, model)

        print "Calling child constructor"

    def childMethod(self):
        print "Calling child method"