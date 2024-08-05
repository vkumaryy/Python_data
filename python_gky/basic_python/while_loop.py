#while loop

a = 1
while a <= 10:
    print(a)
    a += 1 

a = 1
while a <=5 :
    print(a)
    a +=1 
else:
    print("while condition false")


i = 0 
while True:
    i += 1
    print(i)
    if ( i == 3):
        break
print("rest of the code")

u = 1
while u <=3:
    print("outer loop", u)
    u += 1
    j = 1
    while j <= 5:
        print("inner loop", j)
        j += 1
print("rest of the code")