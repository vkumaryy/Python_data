# range(i, j , k) == i , i +k , i+ 2k , i +3k , .. j -1

"""
1. all arrgument must be intergs, wheather its positive or negative

2 . you can not pass a string or float number or any other type in start, stop and stepsize

the stepsize value should not be zero


"""

a = range(15, 20, 2)
print(a)
print(type(a))

for i in a:
    print(i)