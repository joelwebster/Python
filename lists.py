# lists
l = [1,2,3]
print "Lists use square brackets: ", l

# nested lists
l2 = [l,2,3,[4,5]]
print "List within a list (nested): ", l2

# sets contain no duplicates
s = {1,2,3,3,3,4}
print "This is a set: ", s

# tuples are immutable (read-only)
t = ('joel',"james",3)
print "This is a tuple: ", t

print "Lengths: "

print len(l)
print len(l2)
print len(s)
print len(t)

# check emptiness
e = {}

if not e:
    print "Empty"
elif e:
    print "Not empty"