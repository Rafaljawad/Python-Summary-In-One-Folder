#ord method display the ascii number for spesfic char
print(ord("r"))#o/p 114
print(ord("R"))#o/p 82
print(ord(" "))#o/p 32
print(ord("V"))#o/p 86
print(ord("A"), ord("Z") , ord("a"),ord("z") , ord("0"), ord("9"))#o/p 65 90 97 122 48 57


#char convert the ascii to char
print(chr(114))#o/p r
print(chr(82))#o/p R



for ch in "Python":
    print(ord(ch) , end=" ")#o/p 80 121 116 104 111 110 
print("*******************************","\n")
for ch in "उऊऋ":
    print(ord(ch) , end = " ")



    #******************************print function******************************************
# It is used to print the information or objects data to the console
# syntax:

# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

studentname = "Hemanth"
stud_name = 'Venkatesh'

print("Hi ",studentname, sep="/")# sep will separate hi and student name by /

print("Hey ",stud_name,sep="&")



a = 10
b = "is Even "
c = "and it is True"
print(a,b,c , sep='&')#o/p 10&is Even &and it is True


print(a,b,c , sep="**")

print(a,b,c , sep="\n") #new line


print(a,b,c , sep="\t")
# \n = new line
# \t = tab spaces (4 spaces)




#print of empty gives new line
print()#o/p newline




star = "***"
and_ ="&&&&&&&"

print(star)
print()
print()
print()
print()
print()#empty print() > new line
print(and_)

'''o/p   ***


space baecause we have 4 empty print


&&&&&&&'''




print(print(print(print())))
#o/p
"""
None
None
None"""

#**********************COMMENTS*************************************************
# Comments
# computer programming, a comment is a programmer-readable explanation or annotation in the source code of a computer program.

# They are added with the purpose of making the source code easier for humans to understand, and are generally ignored by compilers and interpreters.

# They are non executable statements (lines)

# 2 types of comments in python

# single #
# multiline ''' ''''


#PYTHON IS EASY TO LEARN #SINGLE COMMENT

""" PYTHON
IS
EASY 
TO 
LEARN 
LANGUAGE 
"""      #MULTI LINE COMMENT


#************************************************************