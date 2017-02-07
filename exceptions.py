# exception handling

while True:
    try:
        n = raw_input("Enter an integer: ")
        n = int(n) # convert to int
        break
    except ValueError:
        print "No valid integer"
print "Thanks for entering a valid integer"

#