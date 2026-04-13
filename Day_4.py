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
# num=int(input("Enter any number : "))
# if(num%3==0 and num%5==0):
#     print("Divisible by both 3 and 5")
# elif(num%3==0):
#     print("Divisible by 3 only")
# elif(num%5==0):
#     print("Divisible by 5 only")
# else:
#     print("Divisible by None") 

#Q9. Take marks and assign grade: # ≥90 → A # 80–89 → B # 70–79 → C # <70 → D
# marks=int(input("Enter your marks : "))
# if(marks>=90):
#     print("A")
# elif(marks>=80 and marks<=89):
#     print("B")
# elif(marks>=70 and marks<=79):
#     print("C")
# else:
#     print("D") 

#Q10. Take age and check: # <18 → minor # 18–60 → adult # 60 → senior citizen
# age=int(input("Enter your age : "))
# if(age<18):
#     print("Minor")
# elif(age>=18 and age<=60):
#     print("Adult")
# else:
#     print("Senior Citizen") 

#Q11. Take a number and check: if it is a multiple of 7 and also check if it is even or odd
# a = int(input("Enter any number : "))
# if(a%7==0):
#     if(a%2==0):
#         print("Divisble and even")
#     else:
#         print("Divisible and odd") 
# else:
#     print("Not divisible")  

#HARD

#Q12. Take three numbers and print: greatest / smallest
# a = int(input("Enter any number : "))
# b = int(input("Enter any number : "))
# c = int(input("Enter any number : "))
# if(a>b and a>c):
#     print("A is greatest")
# elif(b>a and b>c):
#     print("B is the greatest")
# else:
#     print("C is the greatest") 

#Q13.Take a year and check whether it is a leap year (Hint: divisible by 4, but special case with 100 and 400)
# year = int(input("Enter any year : "))
# if(year%400==0):
#     print("Leap year")
# elif(year%4==0 and year%100!=0):
#     print("Leap year")
# else:
#     print("Not") 

#Q14. Take a number and classify it as: single digit two digit three digit more
#num = int(input("Enter any number : "))
# if(num>=1 and num<10):
#     print("1 digit")
# elif(num>9 and num<100):
#     print("2 digit")
# elif(num>=100 and num<1000):
#     print("3 digit")
# elif(num>999):
#     print("4 digit and more") 

#Q15. Take age and salary: # age ≥ 21 AND salary ≥ 25000 → Eligible for loan # else → Not eligible
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))
if(age<21):
    print("Not Eligible")
elif(age>=21):
    if(salary>=25000):
        print("Eligible for loan")
    else:
        print("Not Eligible") 