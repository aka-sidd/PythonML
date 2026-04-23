"""Strings"""

str = "A" # All Character has unicode
print(ord(str))
a = 65
print(chr(a))

"""Access the individual character of the strings"""
name = "Siddharth"
print(name[0])
print(name[1])
print(name[5])

"""String Slicing"""

str1 = "Siddharth Engineer"
print(str1[0::1])
print(str1[10::1])
print(str1[0::])
print(str1[::])
