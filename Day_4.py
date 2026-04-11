# DAY - 4 

#EASY

#Q1. Take a number and check whether it is:
# positive negative zero
# num = int(input("Enter any number : "))
# if(num>0):
#     print("Positive")
# elif(num<0):
#     print("Negative")
# else:
#     print("Zero") 

#Q2.Take a number and check whether it is even or odd.
# num = int(input("Enter any number : "))
# if(num%2==0):
#     print("Even Number")
# else:
#     print("Odd Number") 

#Q3.Take a number and check whether it is divisible by 5.
# num = int(input("Enter any number : "))
# if(num%5==0):
#     print("Divisible by 5")
# else:
#     print("Not divisible") 

#Q4.Take marks as input and print:
# "Pass" if marks ≥ 40 "Fail" otherwise
# marks=int(input("Enter the marks obtained : ")) 
# if(marks>=40):
#     print("Passed")
# else:
#     print("Failed")

#Q5. Take age as input and check:
# eligible to vote (≥18)  not eligible otherwise
# age = int(input("Enter your age : "))
# if(age>18):
#     print("Eligible to vote")
# else:
#     print("Not eligible") 

#Q6. Take two numbers and print the greater number.
# a=int(input("Enter a number : "))
# b=int(input("Enter a number : "))
# if(a>b):
#     print("A is greater")
# else:
#     print("B is greater") 

#MEDIUM

#Q7.Take three numbers and print the greatest among them.
# a=int(input("Enter number a "))
# b=int(input("Enter number b "))
# c=int(input("Enter number c "))
# if(a>b and a>c):
#     print("a is greatest")
# elif(b>c):
#     print("b is the greatest")     
# else:
#     print("c is the greatest") 


#Q8.Take a number and check:
# divisible by both 3 and 5 # only by 3 # only by 5 # neither
num=int(input("Enter any number : "))
if(num%3==0 and num%5==0):
    print("Divisible by both 3 and 5")
elif(num%3==0):
    print("Divisible by 3 only")
elif(num%5==0):
    print("Divisible by 5 only")
else:
    print("Divisible by None") 


#Q9. Take marks and assign grade:

# ≥90 → A
# 80–89 → B
# 70–79 → C
# <70 → D
# 10

# Take age and check:

# <18 → minor
# 18–60 → adult

# 60 → senior citizen

# 11

# Take a number and check:

# if it is a multiple of 7
# and also check if it is even or odd
# 12

# Take two numbers and check:

# if they are equal
# if not, print the greater one
# 13

# Take a number and check whether it lies:

# between 10 and 50 (inclusive)
# outside this range