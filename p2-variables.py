"""
Variables
Think of a variable as a name attached to a particular object. In Python, variables need not be declared or defined in advance, as is the case in many other programming languages. To create a variable, you just assign it a value and then start using it. Assignment is done with a single equals sign (=):

A Varible is nothing but giving a name to the memory location(s) to store the value , so that we can reuse that value whenever needed.

It possess a Variablity property , it can change its value during the phase of execution

Rules to define a variable
A variable name must start with a letter or the underscore character.
A variable name cannot start with a number.
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
No Variable can't have the same name as a reserved word.
"""


#Fundamental Data Type

# int = 10, 30 
#  float = 10.21 , 0.1
#  char = 'a' ,'b' ,'c'
#  boolean = True , False
#  String = "Hemanth" , "python" . "729yh2992^*@^*@"
#  complex = 10+2j


age=30
print(age)
print(type(age))#int
#type(variable_name) : check the datatype of the Var


age = "a"
print(age , type(age))#string


age = True
print(age , type(age))#bool


age = 10+2j
print(age , type(age))#complex



#valid variable names

name = "Snowy"
Age = 8
is_pet = True
name = 10.21

print(name , Age , is_pet , sep="\n") #\t = TAB \n = new line



# invalid variable names

# 98_age = 30 #it gives the error  because it started with a num


age_98=30# valid because it ended with a num
print(age_98)



_ = "Hello"# valid _
print(_, type(_))



import keyword# gives all keword in python 

print(keyword.kwlist)
""" o/p ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']"""



#id to know the adress in the memory

a=10
b=10
c=10
print(id(a) , id(b) , id(c))# same memory adress because they carry same val

b=b+2
c=c-1

print(id(a) , id(b) , id(c))# b and c now changed so they have  diffrent adress except a same



#assign a single value to mutliple variables
a = b = c =1729
#assign a different values to mutliple variables in one line
a,b,c = 1729,10,12
print(a,b,c,sep="\n") #\n = new line


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)#apple
print(y)#banana
print(z)#cherry


""" Naming styles
Camel Case:
Second and subsequent words are capitalized, to make word boundaries easier to see.
    Example: numberOfCollegeGraduates

    for naming functions

Pascal Case: 
Identical to Camel Case, except the first word is also capitalized.
    Example: NumberOfCollegeGraduates

    for naming Classes

Snake Case: 
Words are separated by underscores.
    Example: number_of_college_graduates
    for  naming variables"""





# Casting
# If you want to specify the data type of a variable, this can be done with casting.
# #int - float

a = 10

print(float(a))#10.2


#float - int

b = 10.2863

print(int(b))#10


#str - int 

c = "10"

print(int(c))#10


#int -- str

d = 10290903

print(str(d))#"10290903"




#****************************************************************
""" Data types
In programming, data type is an important concept.

It defines the type of Data we use.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type: str

Numeric Types: int, float, complex

Sequence Types: list, tuple, range

Mapping Type: dict

Set Types: set, frozenset

Boolean Type: bool

Binary Types: bytes, bytearray, memoryview"""




#int 
int_var = 5

print(int_var)

print(type(int_var))

int_var = 10.2 #float 

print(type(int_var))

# bin()# to convert the number to binary
# oct()# to convert the number to octal
# hex()# to convert the number to hexadecimal
print(oct(520))
print(bin(2))#o/p 10






#**********************Global Variables*************************************
x = "awesome"#global var

def myfunc():
    print("Python is " + x)

myfunc()


"""If you create a variable with the same name inside a 
function, this variable will be local,
and can only be used inside the function.
The global variable with the same name will remain as it was,
global and with the original value."""

x = "awesome"#global for all inside and outside the function

def myfunc():
    x = "fantastic"#local for only function
    print("Python is " + x)

myfunc()

print("Python is " + x)



""" The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword."""

def myfunc():
    global x# global will let anything outside the wsun uses x (before global x is just available for function)
    x = "awesome"
    print("Python is " + x)

myfunc()
print("Python is " + x)


#Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
    global x# now x has changed to "fantastic" because of global keyword
    x = "fantastic"

myfunc()

print("Python is " + x)




print(bool(0))#false
print(bool(1))#true
print(bool("python"))# bool of any value is true
print(bool(""))# bool of any empty value is false
print(bool(" "))# bool of space is true


a=True
print(int(a))# 1 int of bool is 1 if true and 0 if its false
print(float(a))#1.0 

b=False
print(int(b))# 0 int of bool is 1 if true and 0 if its false
print(float(b))#0.0

c="python"
print(bool(c))# bool of value is true
d=""
print(bool(d))#bool of nothing is false


#all gives Flase
print(bool([])) #empty list
bool(()) #empty tuple
bool({}) #empty set or dictionary
bool(0) #integer 0
bool(0.0)
bool("") #empty string


#**bool of o is always false and bool of any number is always true
#bool of empty is always false and bool of any char or string is always true


#*******************************************************************
'''Naming styles
Camel Case:
Second and subsequent words are capitalized, to make word boundaries easier to see.
    Example: numberOfCollegeGraduates

    for naming functions in python

Pascal Case: 
Identical to Camel Case, except the first word is also capitalized.
    Example: NumberOfCollegeGraduates

    for naming Classes

Snake Case: 
Words are separated by underscores _.
    Example: number_of_college_graduates
    for  naming variables'''


# Use of the underscore character is significant as well. Each of the following defines a different variable(all valid):

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
ega = 10







#assign a single value to mutliple variables
#instead of defining same values for diffrent var we can do it this way:

a = b = c ="hello"
print(a,b,c) #o/p hello hello hello



name = "Adam" #string 
age = 25 #int
Master_degree = True #boolean 
percentage = 7.9  #float
complex_num = 6+5j #complex
print("variable","type of variable","id of variable",sep="----")
print(name, type(name), id(name),sep="----")
print(age,type(age),id(age),sep="----")
print(Master_degree, type(Master_degree), id(Master_degree),sep="----")
print(percentage, type(percentage), id(percentage) ,sep="----")
print(complex_num, type(complex_num), id(complex_num),sep="----")





####*****note **** some keywords like if , string, int , while can not be assigned to variables.
# if=3
# while="hello"
# for=5
# ......etc kewords is all reserved and its not valid to name var using these keywords
#all in valid



