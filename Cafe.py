# class definition
class Cafe(object):
    bankrupt = False

    # class constructor
    def __init__(self, name, location, funds):
        self.name = name
        self.location = location
        self.funds = funds

    # class method
    def open_branch(self):
        if not self.bankrupt and self.funds > 100:
            print "Branch opened."
        elif self.bankrupt or self.funds < 100:
            print "Branch not opened."

    def set_bankrupt(self):
        setattr(self, 'bankrupt', True)  # set bankrupt true

    def is_bankrupt(self):
        if getattr(self, 'bankrupt'):
            print getattr(self, 'name') + " is bankrupt."


c = Cafe("Cafe One", "Paris", 90.00)  # construct Cafe object

# open non-bankrupt branch
c.open_branch()

# open bankrupt branch
c.set_bankrupt()
c.is_bankrupt()
c.open_branch()

print getattr(c, 'location')  # get Cafe location
