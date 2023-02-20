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
lst = [10,10.2892,True,"Kumar",10+2j,None]
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









