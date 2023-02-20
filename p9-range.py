'''
range
It is also sequence data type to generate collection of data in specified range

mainly used for loops

'''

range(0,10,1)

# range(start,stop,step)

#  Stop = must
#  start = 0
#  step = 1
#  stop is exclusive (it's not included) (-1)
#starts from index 0 and stop until index9 and increment by 1


print(list(range(1,10,2)))#starts from index1 and increment by 2(step) until becomes lass than 10(stop) in this case the last item is 9 less than 10 so [1, 3, 5, 7, 9]


print(tuple(range(0,10,2)))#(0, 2, 4, 6, 8)

print(set(range(0,10,1)))#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


print(list(range(0,1,10)))#[0] because 10 >1

print(list(range(10,0,-1)))#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



print(list(range(1,-10,-2)))#[1, -1, -3, -5, -7, -9]