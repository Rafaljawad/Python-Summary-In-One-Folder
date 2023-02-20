x="hello"
print(x)



#Multiline Strings
a=''' lorem ipsuim\n my name \n
python
lover9s'''
print(a)


""" Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string."""



# print('It's a book') #invalid because of single quotes
print('It\'s a book')#valid \ fixes the quote issues also double quotes

print("It's is book") #method1
print('It\'s is a book') # method2




a = "Hello, World!"
print(a[1])# e

for char in a:
    print(char, end="\t")




""" String Length
To get the length of a string, use the len() function."""

print(len(a))#13 





"""" Check String
To check if a certain phrase or character is present in a string, we can use the keyword in."""

txt = "The best things in life are free!"
print("free" in txt)#true


if "best" in txt:
    print(True)



""" Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in"""

txt = "The best things in life are free!"
print("expensive" not in txt)#true
print(dir(txt))# dir displays all the available methods on spesfice var


print(txt.upper())# upper method convert all characters of string to upper case
print(txt.lower())# lower method converts all char to lower case


stra="python is a lovely language"
print(stra.count("a"))# count method counts how many spesfic char are available in the string
print(stra.count("la"))


#input method always return string output
input1=input( "enter your name: ")
print(type(input1))#str
print(bool(input1))#true
if input1:
    print("available")
else:
    print("no data please enter valid data")




# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

str_="hello world"
print(str_[0:4:1])#start from index 0 (include) and stop on index 4(exclude) and move(incrment 1) o/p hell
print(str_[0:4:2])#start from index 0 (include) and stop on index 4(exclude) and move(incrment 2) o/p hl
print(str_[-1:0:-1])#reverse
print(str_[:5])# means go from 0 and stop on index5 by defualt increment by 1
print(str_[::-1])# abrevation for reverse
print(str_[-2:4:-1])# start from index -2(l) and stop on index 4 (o) increment 1 o/p lrow 
print(str_[0:4])




#string is imutable(we can not change the characters)
str_="python"
# str_[0]='m'
# print(str_)#error because string is imutable



#split method (if there is  a string with no space , split method return the string with one index ['python'])
splitList=str_.split()
print(splitList)


#here the string with spaces so the split method will return a list with all letters['p','y','t','h','o','n']
lang = "P y t h o n".split()
print(lang)
# lang[0] = "J"
print(lang)


#join method convert all the items in the list into string (we decide how to join them by putting space or any charecter between "".join,by defult an empty"" means no space)
lang = " ".join(lang)#space 
print(lang)#P y t h o n
lang = "-".join(lang)
print(lang)#P-y-t-h-o-n
lang = "_".join(lang)
print(lang)#P_-_y_-_t_-_h_-_o_-_n because the code run line by line and lang already joined by -





a = "a b A B C D e K r 10 30 &".split()

print(a)#['a', 'b', 'A', 'B', 'C', 'D', 'e', 'K', 'r', '10', '30', '&']

a.reverse()

print(a)#['&', '30', '10', 'r', 'K', 'e', 'D', 'C', 'B', 'A', 'b', 'a']

a.sort() #ascii

print(a)#['&', '10', '30', 'A', 'B', 'C', 'D', 'K', 'a', 'b', 'e', 'r']


for ch in "a b A B C D e K r 10 30 &":
    print(ch , ord(ch) , sep="->")