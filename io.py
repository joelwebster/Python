# input, output, file reading/writing
import os

# input
def get_details():

    name = raw_input("Please enter your name: ")
    print "Welcome " + name
    dob = raw_input("Please enter your date of birth in the format 'DDMMYYYY': ")
    print "Thank you " + name

    # format dob
    day = dob[:2]
    month = dob[2:4]
    year = dob[4:8]
    dob_formatted = day + "/" + month + "/" + year

    # write to file
    fo = open(name + ".txt", 'wb')
    fo.write("Name: " + name + os.linesep)
    fo.write("DOB: " + dob_formatted)
    fo.close()

def read_file(filename):

    # read from file
    fo = open(filename, 'r')    

    # read a number of bytes
    #read = fo.read(100)
    #print os.linesep + read

    # read line
    print "\nReading line: " + fo.readline()
    print "Reading line: " + fo.readline()

    fo.close()

def read_alt(filename):
    with open(filename, 'r') as f:
        read_data = f.read()
        print read_data
    f.closed

# main
get_details()

filename = raw_input("Enter the file name you wish to open: ")
read_file(filename)

filename = raw_input("Enter the file name you wish to open: ")
print "\nReading using alternative method: "
read_alt(filename)