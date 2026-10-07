#Operators are Symbol that perform operations on variables and values. Python has several types of Operators for different 
#task like arithmetic, comparison,logical, and many more
#Arithmetic Operations:-
#Arithmetic Operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc.

a = 12
b = 20
print("Addition of a and b is:",a+b)
print("Subtraction of a and b is:",a-b)
print("Multiplication of a and b is:",a*b)
print("Division of a and b is:",a/b)
print("Modulus of a and b is:",a%b)
print("Exponent of a and b is:",a**b)
print("Floor Division of a and b is:",a//b)
print(12+4/2)

#Assignment Operators:-
#Assignment Operators are used to assign values to variables. The basic assignment operator is the equal sign (=).
a = 20
print(a+20) 
a = 30
a = 40
print(a)   
b = 20
b+=20
b+=40
b+=60
print(b)
#Above operations are compound assignment Operators 

#Comparison Operators:-
#Comparison Operators are used to compare two values. The result of a comparison is a Boolean value
#Comparison Operators are also called Relational Operators, are used to compare two values.
#Comparison Operators will return either True or False according to the condition.
print(12>10)
print(12<10)
print(12==10)
print(12!=10)
print(12>=10)
a = 12.1
b = 12
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(45<67)

#Comparison Operators will work with numbers but you can use them with strings also. The comparison will be done on the basis of ASCII values of the characters in the string.
print("Alice" < "Bob")

print(ord("A"))
print(ord("B"))
print(ord("a"))
print(ord("b"))

#Logical Operators:-
#Logical Operators are used to combine multiple conditions. The main logical operators are and, or, and not.
#and - Returns True if both statements are true
#or - Returns True if one of the statements is true
#not - Returns True if the statement is false
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

#Some Trivial Questions
print(10 > 5 and 10 < 20)
print(10 > 5 or 10 < 20)
print(not (10 > 5)) 