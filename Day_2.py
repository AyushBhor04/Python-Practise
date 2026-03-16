# DAY - 2 
# Q1.Write a program that asks the user to enter their name and prints:
# Welcome <name>
# name=input("Enter your name :")
# print("Your username is ",name) 

# Q2.Write a program that takes any value from the user and prints:
# the value & its datatype.
# value=input("Enter any value: ")
# print(type(value),value)   

# Q3.Write a program that asks the user to enter a number and prints the number along with its datatype.
# value=int(input("Enter any value: "))
# print(type(value),value)

# Q4.Write a program that takes the following inputs from the user:
# name age marks
# Then print them in a clear format.
# name = input("Enter your name :")
# age = input("Enter your age :")
# marks = input("Enter your marks :")
# print("My name is",name,"age being",age,"have scored",marks) 

# Q5.Write a program that asks the user to enter two numbers and prints their sum.
# num_1=int(input("Enter any number: "))
# num_2=int(input("Enter any number: "))
# print("Sum = ",num_1+num_2)

# Q6.Write a program that asks the user to enter one number and prints its square.
# num = int(input("Enter a number:"))
# print("Squared value:",num**2)

# Q7.Write a program that asks the user to enter two numbers and prints their average.
# num_1=int(input("Enter any number: "))
# num_2=int(input("Enter any number: "))
# avg=(num_1+num_2)/2
# print("Average = ",avg) 

# Q8.Write a program that asks the user to enter the side of a square and prints the area of the square.
# side = int(input("Enter side of the square :"))
# print("Area = ",side**2) 

# MEDIUM

# Q9.Write a program that takes two numbers from the user and prints:
# their sum # their difference # their product # their division.
# num_1=int(input("Enter any number: "))
# num_2=int(input("Enter any number: "))
# print("Sum = ",num_1+num_2)
# print("Difference = ",num_1-num_2)
# print("Product = ",num_1*num_2)
# print("Division = ",num_1/num_2) 

# Q10.Write a program that takes two numbers a and b from the user and prints whether a is greater than b.
# a=int(input("Enter any number: "))
# b=int(input("Enter any number: ")) 
# print(a>b) 

# Q11.Write a program that takes two numbers a and b from the user and prints whether a is greater than or equal to b.
# a=int(input("Enter any number: "))
# b=int(input("Enter any number: ")) 
# print(a>=b) 

# Q12.Write a program that takes two floating numbers from the user and prints their average.
# a=float(input("Enter any number: "))
# b=float(input("Enter any number: ")) 
# print("Average = ",(a+b)/2)  

# Q13.Write a program that asks the user to enter length and width of a rectangle and prints its area.
# len = int(input("Enter length "))
# bre = int(input("Enter breadth "))  
# print("Area of rectangle = ",len*bre) 

# Q14.Write a program that asks the user to enter two numbers and prints the remainder when the first number is divided by the second number.
# a=int(input("Enter a "))
# b=int(input("Enter b ")) 
# print("Modulus = ",a%b)  

# HARD

# Q15.Write a program that asks the user to enter three numbers and prints their average.
# a=float(input("Enter any number: "))
# b=float(input("Enter any number: ")) 
# c=float(input("Enter any number: "))
# print("Average = ",(a+b+c)/3)  

# Q16.Write a program that asks the user to enter two numbers and prints True if the first number is divisible by the second number, otherwise False.
# a=float(input("Enter any number: "))
# b=float(input("Enter any number: ")) 
# if(a%b==0):
#     print("true")
# else:
#     print("False") 



# Q17.Write a program that asks the user to enter: # name # age # city 
# # Then print a sentence like:
# My name is ___, I am ___ years old and I live in ___.
name = input("Enter name ")
age = input("Enter age ")
city = input("Enter city ") 
print("My name is ",name+"I am ",age+"years old","I live in ",city)  

# Q18.Write a program that takes two numbers as strings, converts them into integers, and prints their sum.
# a=input("Enter any number: ")
# b=input("Enter any number: ") 
# c=int(a)
# d=int(b)
# print(c+d)  