'''
tuple
It is also used to store multiple items in a single variable.
indexing starts from 0 to n-1
stores heterogenous data
Tuple is immutable , changes are not at locations
Declares with ()
'''

sample = 10,
print(type(sample))#tuple
#when comma comes after number it means the type of this data is tuple

sample = 10,20
print(type(sample))#tuple

sample1 = (20,20,40,30)
print(type(sample1))#tuple

# sample1[0]=10
# print("^^^^^",sample1)#error we can not change because tuple is imutable

print(sample1[0])
#we can do loop as we did with list 
for i in range(len(sample1)):
    print(sample1[i])





b=(10)
print(dir(())) #tuple






'''tuple methods
Python has two built-in methods that you can use on tuples.

count() Returns the number of times a specified value occurs in a tuple
index() Searches the tuple for a specified value and returns the position of where it was found'''