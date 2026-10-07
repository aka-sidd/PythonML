# LOOP FLOW DIAGRAM
#
#                       .-----------------.
#                     (    START PROGRAM    )
#                       '--------+--------'
#                                |
#                    .-----------v------------.
#                   ( Choose a range of values )
#                    '-----------+------------'
#                                |
#                    .-----------v------------.
#                   (   Is another value left?  )
#                    '------+-------------+---'
#                           | YES         | NO
#                           |             |
#                    .------v------.      |
#                   ( Run the code  )      |
#                    '------+------'      |
#                           |              |
#                           '------->------'
#                           (repeat loop)
#                                          |
#                                .---------v---------.
#                              (    END PROGRAM       )
#                                '-------------------'
#
# Examples used below:
#   range(5)       -> 0, 1, 2, 3, 4
#   range(1, 20, 2)-> 1, 3, 5, ..., 19
#   range(10, 0, -1)-> 10, 9, 8, ..., 1
#
# TABLE LOOP
#
# (Enter table number) -> [i = 1] -> [print table line]
#                                  |
#                                  v
#                         [increase i by 1]
#                                  |
#                         <is i <= 10?>
#                           YES |    | NO
#                               |    '----> (END)
#                               '----------> repeat
#
# Loops in Python execute a block of code repeatedly until the range ends.
# There are two main types of loops in Python: for loops and while loops.
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
#        #|
       #|
       #|
       # 100 times.. then its not possible to write print statement 100 times..so we use Loops 
       #1) For Loop:- A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. It allows you to execute a block of code for each item in the sequence. for i in range(5)

for i in range(5):
    print("Hello World")

a = range(1,20,2) #start,stop,step
for i in a:
    print(i)

#Reverse order
for i in range(10,0,-1):
    print(i)


for i in range(-5, -16, -1):
    print(i)

for i in range(5,51,5):
    print(i)

#Some Questions based on For-loops
#1) Accept a number and print Hello world n times
# number = int(input("Enter a number: "))
# for i in range(number):
#     print("Hello World")

# #Print Natural numbers from 1 to n
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i)

# #Reverse Natural numbers from n to 1
# n  = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     print(i)

table = int(input("Enter a number to print its table: "))
for i in range(1,11):
    print(f"{table} x {i} = {table*i}")

    