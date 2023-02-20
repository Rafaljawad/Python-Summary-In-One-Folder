stra="python is a lovely language"
print(stra.count("a"))# count method counts how many spesfic char are available in the string


txt = "The best things in life are free!"
print(dir(txt))# dir displays all the available methods on spesfice var
print(txt.upper())# upper method convert all characters of string to upper case
print(txt.lower())# lower method converts all char to lower case
print(len(txt))# len returns the length 
print(type(txt))# type returns the type of data

import random
x=random.randint(0,10)# return random values
print(x)

# built-in methods
# Math Function Description
#count method it counts spesfic things we give 
s="hello"
print(s.count("l"))#o/p 2     -->2 l in hello string
# abs() Returns absolute value of a number
b=-13
print(abs(b))#13

# divmod() Returns quotient and remainder of integer division

print(divmod(10,3))#res=3 and reminder=1 gives tuple of result and reminder o/p(3,1)
print(divmod(10,2))#res=5 and reminder=0    o/p(5,0)

# max() Returns the largest of the given arguments or items in an iterable
s=[1,4,7,8,9,111]
print(max(s))# 111


# min() Returns the smallest of the given arguments or items in an iterable
s=[1,4,7,8,9,111]
print(min(s))# 1


# pow() Raises a number to a power
print(pow(3,2))
#or
print(3**2)


# round() Rounds a floating-point value
n=12.567488
print(round(n,2))#12.57


# sum() Sums the items of an iterable
s=[1,4,7,8]
print(sum(s))



# dir() to list all functions of object
print(dir(s))



# type() to check the data type of the object
print(type(s))


# len() to count all objects
print(len(s))

#real method converts from complex to real it takes just the real part (number without j)
com_var = 6+3j
print(com_var.real)#o/p 6.0


#imag mathod converts complex to imaginary (it takes only the number with j)
print(com_var.imag)#o/p 3.0


#conjugate converts from add complex to subtract
com_var.conjugate()# 6-3j


# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

str_="hello world"
print(str_[0:4:1])#start from index 0 (include) and stop on index 4(exclude) and move(incrment 1) o/p hell
print(str_[0:4:2])#start from index 0 (include) and stop on index 4(exclude) and move(incrment 2) o/p hl
print(str_[-1:0:-1])#reverse
print(str_[:5])# means go from 0 and stop on index5 by defualt increment by 1
print(str_[::-1])# abrevation for reverse
print(str_[-2:4:-1])# staert from index -2(l) and stop on index 4 (o) increment 1 o/p lrow 


#append -->add items to the list
lst = []
lst.append("Mi")
lst.append("Nokia")
print(lst)#o/p ['MI','Nokia']
lst.append("One plus")
print(lst)#o/p ['MI','Nokia','One Plus']


#clear--->clear the entire list(empty)
lst2=[1,3,6,9,0]
lst2.clear()
print(lst2)#o/p []
