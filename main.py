import time, calendar;

string = "Hello"
string2 = " World"
string3 = string + string2

list = ['joel','webster',123,456]

print(list)

print(list[1])

print (list[:3])

print(string3)

print(string3 * 4)

print(string3[:4])

def function(a,b) :
    c = a * b
    return c

print (function(2,4))

print(function(a=2,b=3))

# lambda function
sum = lambda a,b : a + b;

print(sum(10,20))

# default function arguments
def printInfo(name,age=20):
    print "Name: ",name
    print "Age: ",age

printInfo("Joel")
printInfo(name="Joel")
printInfo("Joel",25)

# dictionary
dict = {'Name':'Joel', 'Age':'25', 'Gender':'Male'}

print dict['Name'], dict['Age'], dict['Gender']

dict['Work'] = 'SBC'

print dict['Work']

print "Dictionary keys: ", dict.keys()
print "Dictionary values: ", dict.values()


# time
ticks = time.time()
print "Number of ticks since 12:00am, January 1st 1970: ", ticks

# calendar
cal = calendar.month(2017,1)

print cal

calendar.setfirstweekday(6)

# type conversion
int2 = 4
string = "5"
float2 = 23.444445
string2 = "22.555556"

# int to string
x = str(int2)
print x

# string to int
y = int(string)
print y

# string to float
z = float(string2)
print z

# float to string
p = str(float2)
print p

# loop
for letter in "String":
    print letter