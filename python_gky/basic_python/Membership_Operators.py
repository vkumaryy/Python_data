"""
This code snippet checks if a specific substring is present in a given string.

Example Usage:
    st1 = "Welcome to python world"
    print("to" in st1)
    print()
    print("gkye0" in st1)

Inputs:
    st1: A string containing the phrase "Welcome to python world".

Flow:
    1. The code snippet initializes a variable `st1` with the value "Welcome to python world".
    2. It checks if the substring "to" is present in `st1` using the `in` operator. The result is `True` because "to" is present in the string.
    3. It prints a blank line.
    4. It checks if the substring "gkye0" is present in `st1` using the `in` operator. The result is `False` because "gkye0" is not present in the string.

Outputs:
    True
    False
"""

st1 = "Welcome to python world"
print("to" in st1)
print()
print("gkye0" in st1)
print()

"""
Check if a substring is not present in a given string.

Args:
    None

Returns:
    None

Example Usage:
    str2 = "Welome to the python world"
    print("subs" not in str2)

Explanation:
    The code snippet initializes a variable `str2` with the value "Welcome to the python world". It then checks if the substring "subs" is not present in `str2` using the `not in` operator. The result is `True` because "subs" is not present in the string.
"""

#not in operator
str2 = "Welome to the python world"
print("subs" not in str2)