"""
Check if two variables, `a` and `b`, are referring to the same object in memory.

Inputs:
- `a`: an integer variable with a value of 10
- `b`: a string variable with a value of '10'

Outputs:
- The result of the comparison between `a` and `b` using the `is` operator

Example Usage:
```python
a = 10 
b = '10'

print(a is b)
```
"""

a = 10 
b = '10'

print(a is b)

# is not

# this opertor workd in reverse manner for is opertor 
# it reutrns True if memory location of two object are not same , if they are sme it returns False

print(a is not b)

value = (1+1)*2**4//3+4-1
print(value)