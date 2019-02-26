# your fisrt program - print Hello Python 101
print("Hello Python 101")

# types
print(type(11))
print(type(21.213))
print(type("Hello Python 101"))
print(type(True))

# cast types
print(float(2))
print(int(1.1))
print(int('1'))
print(str(1))
print(str(4.5))
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

# expressions and variables
print(25/6)
print(25//6)

my_variable = 10

total_min = 43+42+57
total_hour = total_min / 60
print(total_hour)

# string operators
Name = 'Michael Jackson'
print(Name[0])
print(Name[-15])
print(Name[0:4])
print(Name[::2])
print(Name[0:5:2])
print(len(Name))

Statement = Name + ' is the best'
print(Statement)
replicate = 3 * Name
print(replicate)
print('Michael Jackson \n is the best')
print('Michael Jackson \t is the best')
print('Michael Jackson \\ is the best')
print(r'Michael Jackson \ is the best')

A = "Thriller is the sixth studio album"
B = A.upper()
print(B)

C = "Michael Jackson is the best"
D = C.replace('Michael','Janet')
print(D)

print(Name.find('el'))
print(Name.find('Jack'))

# lists (mutables) and tuples (immutables)
Ratings = (10,9,6,5,10,8,9,6,2)
tuple1 = ('disco',10,1.2)
print(type(tuple1))
print(tuple1[0])
tuple2 = tuple1 + ('hard rock',10)
print(tuple2)
print(tuple2[0:3])
print(len(tuple2))

Ratings1 = Ratings
print(Ratings1)
Ratings = (2,10,1)

RatingsSorted = sorted(Ratings)

NT = (1,2,("pop","rock"),(3,4),("disco",(1,2)))
print(NT[2])
print(NT[2][1])
print(NT[2][1][0])

L = ["Michael Jackson", 10.1, 1982,[1,2],["A",1],"MJ",1]
print(L.index(1982))
print(L.index(1983))
print(L[0])
print(L[-2])
print(L[5:7])
L1 = L + ["pop",10]
print(L1)

L = ["Michael Jackson", 10.1, 1982]
L.extend(["pop",10])
print(L)
L.append(["pop",10])
print(L)
L.append("A")
print(L)

A = ["disco",10,1.2]
A[0] = "hard rock"
print(A)
del(A[0])
print(A)

"hard rock".split()
"A,B,C,D".split(",")

B = A
A[0] = "banana"
B = A[:]
A[0] = "hard rock"
help(A)

# sets
Set1 = {"pop","rock","soul","hard rock","rock","R&B","rock","disco"}
print(Set1)
L = ["Michael Jackson", 10.1, 1982]
set(L)

A = {"Thriller","Back in Black","AC/DC"}
A.add("NSYNC")
print(A)
A.remove("NSYNC")
print(A)
print("AC/DC" in A)
print("Who" in A)

album_set_1 = {"Thriller","Back in Black","AC/DC"}
album_set_2 = {"The Dark Side of the Moon","Back in Black","AC/DC"}
album_set_3 = album_set_1 & album_set_2
print(album_set_3)
print(album_set_1.union(album_set_2))
print(album_set_3.issubset(album_set_1))

# dictionaries
albums_year = {"Thriller":"1982","The Dark Side of the Moon":"1973","Back in Black":"1980"}
print(albums_year["Thriller"])
del(albums_year["Thriller"])
albums_year["Thriller"] = "1982"
"Thriller" in albums_year
"1990" in albums_year
albums_year.keys()
albums_year.values()

# conditions and branching
a = 6
a == 7
a == 6

i = 7
i > 5
i < 6
i!=6
"AC/DC"=="Michael Jackson"
"AC/DC"!="Michael Jackson"

age = 21
if(age >18):
    print("you can enter")
elif(age == 18):
    print("go see Pynk Floyd")
else:
    print("go see meat loof")
print("move on")

album_year = 1990
if(album_year < 1980) or (album_year > 1989):
    print("The Album was made in the 70's or 90's")
else:
    print("The Album was made in the 1980's")
    
album_year = 1983
if(album_year > 1979) and (album_year < 1990):
    print("The Album was made in the 1980's")
    
# loops
print(range(3))
print(range(10,15))

squares = ["red","yellow","green","purple","blue"]
for i in range(0,5):
    squares[i] = "white"
    
squares = ["red","yellow","green"]
for square in squares:
    print(square)
    
squares = ["red","yellow","green"]
for i,square in enumerate(squares):
    print(square)
    print(i)
    
squares = ["orange","orange","purple","blue"]
Newsquares = []
i = 0
while(squares[i]=="orange"):
    Newsquares.append(squares[i])
    i=i+1
    
# functions
album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]
L = len(album_ratings)
print(L)

S = sum(album_ratings)
print(S)

#   --ordered but not changed
SS = sorted(album_ratings)
print(SS)
#--ordered with changed
album_ratings.sort()
print(album_ratings)
#--making functions
def add1(a):
    b=a+1
    return b

add1(5)

c = add1(10)
print(c)

d = add1(8)
print(d)

def add11(a):
    """add 1 to a"""
    b=a+1
    return b

help(add11)

def Mult(a,b):
    c=a*b
    return c

Mult(5,5)
Mult(10,3.14)
Mult(2,"Michael Jackson ")

def MJ():
    print("Michael Jackson")
    
MJ()

def NoWork():
    pass

print(NoWork())

def add111(a):
    b=a+1;
    print(a,"plus 1 equals",b)
    return b

add111(2)

def printStuff(Stuff):
    for i,s in enumerate(Stuff):
        print("Album",i,"Rating is",s)
        
album_ratings = [10.0,8.5,9.5]
printStuff(album_ratings)

def ArtistNames(*names):
    for name in names:
        print(name)
        
ArtistNames("Michael Jackson","AC/DC","Pink Floyd")
ArtistNames("Michael Jackson","AC/DC")

def AddDC(y):
    x=x+"DC"
    print(x)
    return(x)
    
x = "AC"
z = AddDC(x)
print(z)

def Thriller():
    Date=1982
    return Date

Thriller()
Date

def Thriller1():
    Date1=1982
    return(Date1)
    
Date1 = 2017

print(Thriller1())
print(Date1)

def ACDC(y):
    print(Rating)
    return(Rating+y)
    
Rating = 9
Z = ACDC(1)
print(Z)
print(Rating)

def PinkFloyd():
    global ClaimedSales
    ClaimedSales =  "45 million"
    return ClaimedSales

PinkFloyd()
print(ClaimedSales)

# objects and classes
class Circle(object):
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color
        
    def add_radius(self,r):
        self.radius = self.radius + r

class Rectangle(object):
    def __init__(self,color,height,width):
        self.color = color
        self.height = height
        self.width = width
        
C1 = Circle(10,"Red")
C1.radius
C1.color = "Blue"
C1.color
C1.radius
dir(Circle)

# reading files with open - r for reading, w for writing and a for appending
File = open("/File.txt","r")
File.name
File.mode
File.close()

with open("File.txt","r") as File:
    file_stuff = File.read()
    print(file_stuff)
print(File.closed)
print(file_stuff)
file_stuff

with open("File.txt","r") as File:
    print(File.read(4))

with open("File.txt","r") as File:
    file_stuff = File.readlines()
    print(file_stuff)
    
with open("File.txt","r") as File:
    file_stuff = File.readline()
    print(file_stuff)
    
with open("File.txt","r") as File:
    file_stuff = File.readline()
    print(file_stuff)
    file_stuff = File.readline()
    print(file_stuff)
    
with open("File.txt","r") as File:
    for line in File:
        print(line)
    
with open("File.txt","r") as File:
    file_stuff = File.readlines(4)
    print(file_stuff)
    
with open("File.txt","r") as File:
    print(File.read(4))
    print(File.read(4))
    print(File.read(7))
    print(File.read(15))