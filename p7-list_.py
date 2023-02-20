'''Lists are used to store multiple items in a single variable.
indexing starts from 0 to n-1
stores heterogenous data(diffrent data type)
List is mutable , changes are allowed at locations.
Declared with []'''


student_name = ["Adam","Ali","Rafal","tina",10,10.22,True]#hetrogenous(diffrent data types with in the list)
print(student_name ,type(student_name))
print(student_name[-1] , type(student_name[-1]))#index-1 means is len(list-1)(last item from left to right and the first item from right to left)in this case True



#Homogenious(same data type)
marks = [10,20,30,30,40]
print(marks)

#Hetrogenious(diffrent data type)
lst = [10,10.2892,True,"Tina",10+2j,None]
print(lst)


#list in python is mutable(means we can change the data with in the position )
#mutability = changing the location's data
listy=[1,5,True,10.20]
listy[2]=100#will change the true to 100
print(listy)#o/p [1, 5, 100, 10.2]


l=["nancy"]*10
print(l)#['nancy', 'nancy', 'nancy', 'nancy', 'nancy', 'nancy', 'nancy', 'nancy', 'nancy', 'nancy']





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

#************************LIST COMPREHENSION*******************************
# It shorten the sytax of list with for loops

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#normal for loop syntax:

a=[]
for i in range(20):
    a.append(i)
print(a)
    

#comprehension syntax:
a=[i for i in range(20)]
#it means print i where i is the index with in the range of 20 with no condition
print(a)

# **************************************************************************************
#normal for loop with if statement syntax:
# print even numbers
a=[]
for i in range(20):
    if i%2==0:
        a.append(i)
print(a)
#comprehension syntax with if statement:
a=[i for i in range(20) if i%2==0]
print(a)
# or
a=[i for i in range(0,20,2)]
print(a)

# **************************************************************************************
#odd num
b=[i for i in range(20) if i%2==1]
print(b)


# **************************************************************************************
c=[i*i*i for i in range(10)]#0*0*,1*1*1,2*2*2 ..etc
print(c)



#********************************************************************************
#with in the list try to print the index that has spesfic name
listy=['Nancy','adam','joreg','Ellie']
#with in the listy list find the index that has Ellie and print it
x=[i for i in range(len(listy)) if listy[i]=="Ellie"]
print(x)#index 3

# **************************************************************************************
num=12
d=[ f'{num} * {i} = {num*i}' for i in range(10)]
print(d)

#2D LIST
for row in range(4):
    for col in range(5):
        print(row,col , end="  ")
    print() 


#comprehension
# print 4 rows and each row has 5cols 
array_2d=[[(row,col ) for col in range(5)] for row in range(4)]
print(array_2d)
# **************************************************************************************




# **************************************************************************************




some_a = ["Vemuri","PYTHON",["Swathi","november","python"],("Python","Ruby"),{"AA","BB","AA"}]

print(some_a[0])#Vemuri
print(some_a[-1])#{'AA', 'BB'}
print(some_a[-2][-2])#Python
print(some_a[2][1])#november
print(some_a[-3][-2][-4])#m




#****************** LIST METHODS **************************
'''
Python has a set of built-in methods that you can use on lists/arrays.

append() Adds an element at the end of the list

clear() Removes all the elements from the list

copy() Returns a copy of the list

count() Returns the number of elements with the specified value

extend() Add the elements of a list (or any iterable), to the end of the current list

index() Returns the index of the first element with the specified value

insert() Adds an element at the specified position

pop() Removes the element at the specified position

remove() Removes the first item with the specified value

reverse() Reverses the order of the list

sort() Sorts the list'''

a =[0]*3#this will add 3 indexes each one has 0 [0,0,0]
print(a)
a[0] = "vicky"#change the value at index 0 from 0 to vicky'
print(a)
a[1]= "Python"#change the value at index 1 from 0 to python'
print(a)



#insert method add items to list in a specfic index
x=[3,5,6]
x.insert(0,10)#insert at index 0 value 10
print(x)#o/p[10, 3, 5, 6]


names=['adam','lina','rima']
names.insert(2,['1','mina'])
print(names)
#o/p ['adam', 'lina', ['1', 'mina'], 'rima']


#index () returns the position of item values 
# Return first index of value.
names.index('adam')
print('adam at index: ' , names.index('adam'))


#extend add items to the end of list 
names.extend(['nardin','mary'])
print("list after extend method is :",names)#o/p list after extend method is : ['adam', 'lina', ['1', 'mina'], 'rima', 'nardin', 'mary']

#append vs extend
# append() # only 1
# extend() # more than 1 or add list to the tail of the another tail

#copy
names2=names.copy()
print('names 2 copy list is :',names2)#o/p names 2 copy list is : ['adam', 'lina', ['1', 'mina'], 'rima', 'nardin', 'mary']


print('the adress os names is :',id(names),"the adress of names2 is : ",id(names2))
#id method return the adress the adress has to be diffrent because we made a copy.


#list addition 
print(['Google', 'Microsoft'] + ["Wipro","optum"]) #o/p ['Google', 'Microsoft', 'Wipro', 'optum']


some_names=names #alias
print(some_names,id(some_names),id(names))#same names list and same id in alias case




# copy() method will create a separate block of memory , so ID's will be different
# Changes in one variable will not affect in another variable
#alias = both will have memory locations , change in one variable will affect the other variable



#pop if there is no index by defualt -1
num_list=[3,12,6,8,9]
num_list.pop()#no index estimated o/p 9 will be take out
print(num_list)#[3, 12, 6, 8]
num_list.pop(0)#take out the value at index 0
print(num_list)#[12, 6, 8]

# pop() vs remove()
# pop() -- indexing 
# remove() -- value




#list methods summury
# all list methods
'''append() # only 1
extend() # more than 1 or add list to the tail of the another tail
count()
index()
sort()
reverse()
copy()



#insertion of data
append()
extend()
insert()

#deletion

remove() #based onvalues
clear() #all
pop() #based on loc  #default = -1

#sorting
sort() #revere=True (desc)  , False = ascen

#copy
copy()

#index and counting

index()
count()'''