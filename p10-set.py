'''set
Set is a collection which is unordered and unindexed.

No duplicate members.

Sets are written with curly brackets {}.'''


a="abcaefg"
b = ['ace','ball','count','ace']
print(set(a)) #string to set(it takes each char in the string)o/p {'f', 'c', 'b', 'e', 'g', 'a'}
print(set(b))#it takes each item in the list o/p {'ace', 'ball', 'count'}


fruits = {"apple","banana","grapes","orange","apple",'orange', 10, True}

print(fruits)
print(type(fruits))#set
print(len(fruits))#6 not 7 because set doesnt count duplicate(apple and orange)

#add method --->add items to the set
fruits.add('bluberry')
print(fruits)# because set is unindexed so each time we run we find bluberry in diffrent place like so:
#{True, 'apple', 'orange', 'banana', 'bluberry', 10, 'grapes'}
#{'orange', True, 'grapes', 'apple', 10, 'bluberry', 'banana'}

print(len(fruits))#now its 7


# print(fruits[0])#error #  'set' object is not subscriptable (unindexed each time the item appears in diffrent index)

lst_num= [10,20,30,10,20,20,30]

set_num= {10,20, 30,10,20,20,30}

print(len(lst_num),len(set_num))#7,3(list counts duplicate but set does not count duplicate)

