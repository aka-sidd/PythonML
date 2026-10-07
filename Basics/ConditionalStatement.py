# Conditional statements in Python allow decision-making by executing different
# blocks of code based on conditions.

#                         .-----------------.
#                       (    START PROGRAM    )
#                         '--------+--------'
#                                  |
#                         .--------v--------.
#                       (   Is age >= 18?    )
#                         '----+-------+----'
#                              |       |
#                    TRUE      |       |      FALSE
#                     LEFT      |       |      RIGHT
#                              |       |
#             .----------------v-.   .-v----------------.
#            (   Can vote         ) (   Cannot vote       )
#             '---------+---------'   '--------+---------'
#                       |                        |
#                       '------------+-----------'
#                                    |
#                         .----------v----------.
#                       (      END PROGRAM       )
#                         '---------------------'

age = 20

if age >= 18:
	print("Can vote")
else:
	print("Cannot vote")


# money = int(input("Please give me some money: "))
# if money == 10:
# 	print("I wil have a choco baar")
# elif money == 20:
# 	print("I will have a choco bar and a cold drink")
# else:
# 	print("I will have a choco bar, a cold drink and a burger")

#Now improve this code
money = int(input("Please give me some money: "))
if money < 10:
	print("Money is not enough to buy anything")
elif money >=10 and money<20:
	print("I will have a choco bar")
elif money >=20 and money<30:
    print("I will have a choco bar and a cold drink")
else:
	print("I will have a choco bar, a cold drink and a burger")

#Some Questions are Conditional...
#1) Accept two numbers and print the greatest number between them..
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>num2:
	print(f"{num1} is greater than {num2}")
elif num1<num2:
	print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")

#Accept the gender from the user and print "Good Morning Sir" if the gender is male and "Good Morning Ma'am" if the gender is female.
gen = input("Enter your gender as character (M/F): ")
if gen == "M" or gen == "m":
	print("Good Morning Sir")
elif gen == "F" or gen == "f":
    print("Good Morning Ma'am")
else:
    print("Invalid gender")

# Accept an integer from the user and check whether it is an even or odd number.
num = int(input("Enter an integer: "))
if num%2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")