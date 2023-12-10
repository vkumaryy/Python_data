""" In the cast/explicti type conversion , programmer convert one data type into another data type

int(n)

float(n)

complex(n)

complex(x, y) where x is real part and y is imaginary part

str(n)

list(n)

tuple(n)

bin(n)

oct(n)

hex(n)


"""

"""
Perform division between two variables `a` and `b`, and convert the result to an integer.

Example Usage:
    a = 5
    b = 2
    value = a/b
    print(value)
    int_value = int(value)
    print(int_value)

Expected output:
    2.5
    2
"""

a = 5
b = 2
value = a/b
print(value)
int_value = int(value)
print(int_value)


"""
This code snippet performs an addition operation between the variable `q` and the integer value of the variable `u`. It then prints the result.

Example Usage:
    q = 20
    u = '10'
    print(type(u))
    r = q + int(u)
    print(r)

Expected output:
    <class 'str'>
    30
"""

q = 20
u = '10'
print(type(u))
r = q + int(u)
print(r)