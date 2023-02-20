'''dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values'''



''' note:
    KEY SHould be unique and immutable
    #str
    #tuple
    #int
    #float
    #bool
    #complex
    
    
#not allowed
# - list
# - dict
# - set
# '''


#dictionary syntax
# dictionary = {
#     K1 : v1,
#     K2 : v2,
#     Kn : Vn
# }

nums={3:3,4.1:4}#here are the keys int and float and their values also int and float(allowed)
print(nums[3],nums[4.1])#o/p the value for the key 3 is 3 and the value of key 4.1 is 4


student_name = {"name"  : "Ram",
                "company" : "CS",
                "salary"  : 1400,
                "has driver license":True
                }

print(student_name['name'],student_name['company'],student_name['salary'],student_name["has driver license"],sep="*****")
#o/p Ram*****CS*****1400*****True

#******************* KEYS AND VALUES METHODS ******************************************
print(student_name.keys())#keys method gives all keys in the dict o/p dict_keys(['name', 'company', 'salary', 'has driver license'])
print(student_name.values())#values method gives all values in the dict o/p dict_values(['Ram', 'CS', 1400, True])



sample_dic = {
            "name":"Adam",
            "lang":"Python",
            "IsStudent":True,
            "name":"Noa"
            }
print(sample_dic)
#whene ever you have double keys  , it will consider the latest one
#{'name': 'Noa', 'lang': 'Python', 'IsStudent': True}
#dictionary accept uniqu keys 



print(sample_dic["name"])
print(sample_dic["lang"])
#**************************************************************
#In Dictionary , keys are indexes
for i in sample_dic.keys():#keys method gives keys and we itterate over them 
    print(i)
'''o/pNoa
Python
name
lang
IsStudent'''

for j in sample_dic.values():
    print('*****',j)
# ***** Noa
# ***** Python
# ***** True


for k in sample_dic.keys(),sample_dic.values():
    print(k)
'''o/p dict_keys(['name', 'lang', 'IsStudent'])
dict_values(['Noa', 'Python', True])'''



#*********************GET MeTHOD****************************
#get mathod returns the value of spesfic key and it takes 2 pars one is the key and the other if the givven key is not in the dic
x=sample_dic.get("name","Key not found")#name in dict so o/p noa
print(x)

x=sample_dic.get("school","Key not found")# school key is not in the dic so o/p key not found
print(x)


#if we dont write not found pars so by defult is none
x=sample_dic.get("school")# school key is not in the dic and no string to return  so o/p by defult is none
print(x)





