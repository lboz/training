########################################################
### Object Oriented Programming
########################################################

""" 
Objects: 
    - type
    - internal representation
    - set of procedures for interaction
- data abstraction
- internal represantation
- interface

-  create new instances
- destroy objects - del or .. forget them

- creating a class  //  using an instance for a class
    - class name                     - create new instances
    - attributs                      - operations on the instances
    - code to implement        

Avantages of OOP
- bundle data into packages together with procedures
- divide-and-conquer development
    - easier to reuse the code
    - increse modularity and reduce complexity

Define your own type
- class keyword
class Coordinate(object):    #class definition (class), class name (Coordinate), class parent (object)
    <attributes>
** Coordinate is a subclass of object

- attributes - data and procedures that 'belong' to the class
- 

** how to create an instance:
    - special method called __init__ to initialize some data attributes


class Coordinate(object):
    def __init__(self, x, y)

Methods
- procedural attribute, like a function that works only with this class
- "." operator to access data

- special operators:
    - __ad__(self, other)
    - __sub__(self, other)      # substract
    - __eq__(self, other)
    - __lt__(self, other)       # less than
    - __len__(self)
    - __str__(self)             # print(self)
    - __isistance__             # type

"getters" - getNumber - getDenom ...

    def __str__(object)     # print
    def __isinstance
- representational invariant enforced by the code
    - internal data representation
    - interface - insert(e), member(e), remove(e)
    
# Hierarchy 
    - parent class - superclass
    - child class - subclass
        - inherits all data and behaviors of parent class
        - add more info
        - add more behavior
        - override behavior

# tag variables - used to give unique id to each instance
        
# Building a class
    - 


"""


class Clock(object):
    # special method to create an instance __ is double underscore
    # self - parameter to refer to an instance of the class
    def __init__(self, time):
	    self.time = time

    def print_time(self):
	    time = '6:30'
	    print(self. time)


clock = Clock('5:30')
clock.print_time()

###
class Clock(object):
    def __init__(self, time):
	    self.time = time

    def print_time(self, time):
	    print(time)


clock = Clock('5:30')
clock.print_time('10:30')

###
class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()

#####################

class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def getX(self):
        return x

    def getY(self):
        return y


class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def getX(self):
        return self.x

    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
print(w1.getX())

########################


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    # Add an __eq__ method that returns True if coordinates refer to same point
    # in the plane (i.e., have the same x and y coordinate).
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False   
    
        # Define __repr__, a special method that returns a string that looks
        # like a valid Python expression that could be used to recreate an
        # object with the same value. In other words, eval(repr(c)) == c given
        # the definition of __eq__ from part 1
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'


########################

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __intersect__(self,other):
        """Returns a new intSet containing elements that appear in both sets.
           In other words, s1.intersect(s2)
           ATT - if s1 and s2 have no elements in common
           https://docs.python.org/3/library/stdtypes.html """
        newObj = {}
        for i in self.vals:
            print('i: ' + i)
            if i in other.vals:
                newObj.insert(i)
                print('newObj: ' + newObj)
        return '{' + ','.join(newObj) + '}'
    
    def __len__(self):
        """Returns the number of elements in s"""
        return len(self.vals)
           

#############################
        
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

myAnimal = Animal(3)
print(myAnimal)

myAnimal.set_name('foobar')
print(myAnimal)

myAnimal.get_age()

myAnimal.age        # do not use - not good style

################################

# Hierarchy - Subclasses

class Cat(Animal):
    # adds new functionality
    def speak(self):
        print("meow")
    # overrides __str__ from Animals
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

# create age
jelly = Cat(1)
jelly.get_name()

# add name
jelly.set_name('JellyB')
jelly.get_name()        

print(jelly)                        # cat:JellyB:1
print(Animal.__str__(jelly))        # animal:JellyB:1

blob = Animal(1)
print(blob)                         # animal:None:1
blob.set_name()
print(blob)                         # animal::1

jelly.speak()                       # meow
blob.speak                          # blob is an animal - no speak method there


################################

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)
       
peter = Rabbit(5)        
peter.speak()   
 
################################    
    
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

eric = Person("eric", 45)
john = Person("john", 55)
eric.speak()
eric.age_diff(john)             # eric is 10 years younger than john
Person.age_diff(john, eric)     # john is 10 years older than eric

################################ 

import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
       self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

fred = Student('Fred', 18, 'Course VI')
print(fred)
fred.speak()

#jelly = Cat(1)
#jelly.set_name('Jelly')
#tiger = Cat(1)
#tiger.set_name('Tiger')
#bean = Cat(0)
#bean.set_name('Bean')
#print(jelly)
#jelly.speak()
#blob = Animal(1)
#peter = Rabbit(3)
#peter.speak()
#eric = Person('Eric', 45)
#eric.speak()
#john = Person('John', 55)
#eric.age_diff(john)
#
#fred = Student('Fred', 18, 'Course VI')


#######################################

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
        
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
print(Accio())



#######################################

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

obj = D()

print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
obj.x()
obj.y()
obj.z()

##################################################

# tag variables

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                       and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite





peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')
mopsy = peter + hopsy
print(mopsy == cotton)


#########################################

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''        
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output
    
    
#########################################
#===============================
''' Write a generator, genPrimes, that returns the sequence of prime numbers
    on successive calls to its next() method: 2, 3, 5, 7, 11, ...    
'''

def genPrimes(n):
    prime = []
    for p in (2, range(n)):
        if c%p != 0:
            prime.append(p)
    if all((c%p !=0) for p in prime):
        
p=[]
...
if all(x % p for p in prime):    
    
def genPrimes(n):
    ''' generates the first n primes
    '''
    p = [2]
    c = 2

    while len(p) < n:
        j = 0
        c += 1
        while j < len(p):
            if c % p[j] == 0:
                break
            elif j == len(p) - 1:
                p.append(c)
            j += 1
    print(p)
n = 20
print(genPrimes(n))    
    
    
def genPrimes(number):
    ''' generates primes max n
    '''
    cnt = 0
    for i in range (1, number+1):
        for j in range(1, i+1):
            if(i%j == 0):
                cnt += 1
        if(cnt == 2):
            print(i)
        cnt = 0

number = 20
print(genPrimes(number))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



