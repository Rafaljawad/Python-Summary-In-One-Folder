'''It is used to read the data from the input console or user .
To keep track or dynamic data
by default it will read very data as string type'''
#input function always return string 

my_name=input("enter your name: ")
print(f"my name is:  {my_name}")
print(type(my_name))#str
print(len(my_name))

my_age=input("enter your age: ")
print(f"my age is : {my_age}")
print(type(my_age))#str
#to convert it to int we use int method
my_age=int(input("enter your age: "))
print(type(my_age))#int



sal = input("Enter the salary")

print(sal, type(sal))
sal = float(sal) # map to the same variable (we changed its data type from str to float)
sal2 = float(sal)
print(sal,type(sal2),type(sal))



#will use input ,ethod to make complex number eqation a+bj
real=float(input(" enter real number: "))
imag=float(input(" enter imaginary number number: "))
res=complex(real,imag)
print(f"the complex number is :{res}")#o/p the complex number is :(5+4j)


str_b = "                              "
print(len("Helo"))

print(len(str_b))# 30 space (space are countable)






student_id= int(input("Enter the student id"))
student_rank= bool(input("enter the student pass or fail"))
student_marks= float(input("enter the student marks"))
student_name = input("enter student name")

print(student_id,student_rank,student_marks,student_name)
print(type(student_id),type(student_rank),type(student_marks),type(student_name),sep="******")