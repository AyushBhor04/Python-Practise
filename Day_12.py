#DAY=12

#EASY

#Q1.Create a class Car with attributes brand and color , create 2 objects and print their values.
# class Car:
#     brand="Audi"
#     color="Black"
# o1=Car()
# print(o1.brand)
# print(o1.color)
# o2=Car()
# print(o2.brand) 
# print(o2.color) 

#Q2.Create a class Student with name and age later initialize values using constructor.
# class Student:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age
# s1=Student("Ayush",24) 
# print(s1.name)
# print(s1.age) 

#Q3.Create a class Laptop with brand and price and add a method to display details.
# class Laptop:
#     brand = "HP"
#     price = 70000

#     def dets(self):
#         print(self.brand)
#         print(self.price) 
# o1=Laptop()
# o1.dets() 

#Q4.Create a class Rectangle with length width later add method to calculate area.
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         area=self.length*self.breadth
#         print(area)
# r1=Rectangle(7,9)
# r1.area()   

#Q5.Create a class Circle with radius and add method to calculate circumference.
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def circumference(self):
#         circum=2*(22/7)*self.radius
#         print(circum)
# c1=Circle(7)
# c1.circumference()

#Q6.Create a class Employee with name and salary and add method to print employee details.
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print(self.name)
#         print(self.salary)  
# e1=Employee("Ayush",150000)
# e1.display() 
# e2=Employee("Jay",10000)
# e2.display()
 
#MEDIUM

#Q7.Create a class BankAccount with: account holder balance ; Add methods: deposit withdraw check balance
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name 
#         self.balance=balance 
#     def deposit(self,val):
#         print("Account handler name -",self.name)
#         self.balance=self.balance+val
#         print("Your current balance after deposit is",self.balance)
#     def withdraw(self,val):
#         print("Account handler name -",self.name)
#         self.balance=self.balance-val
#         print("Your balance after current withdraw is",self.balance)
#     def check_balance(self):
#         print("Account handler name -",self.name)
#         print("Your current balance is",self.balance)
# p1=BankAccount("Ayush",1000)
# p1.check_balance()
# p1.deposit(500) 
# p1.withdraw(500)
# p1.check_balance()

#Q8.Create a class Student that takes marks of 3 subjects AND calculates average using method
# class Student:
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks=marks    
#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"your average score is : ",sum/3)
# s1 = Student("Ayush",[98,99,96]) 
# s1.get_avg() 

#Q9.Create a class Calculator with methods add subtract multiply divide
# class Calculator:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#     def sum(self):
#         print(self.x+self.y)
#     def subtract(self):
#         print(self.x-self.y)
#     def multiply(self):
#         print(self.x*self.y)
#     def divide(self):
#         print(self.x/self.y)
# i1=Calculator(9,5)
# i1.sum()
# i1.subtract()
# i1.multiply()
# i1.divide() 
    
#Q10.Create a class Book with: title author price.Add method to display all details.
# class Book:
#     title="Atomic Habits"
#     author="Mayur"
#     price="100"

#     def display(self):
#         print("Title of the book",self.title)
#         print("Author of the book",self.author)
#         print("Price of the book",self.price)
# b1=Book()
# b1.display() 

#Q11.Create a class Mobile with brand model price an add method to apply discount percentage.
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def apply_discount(self, discount_percent):
#         discount_amount = (self.price * discount_percent) / 100
#         self.price -= discount_amount
#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)
# m1 = Mobile("Samsung", "S24", 80000)
# print("Before Discount:")
# m1.display()
# m1.apply_discount(10)
# print("\nAfter Discount:")
# m1.display()

#Q12.Create a class Person with name , age ;Add method:check if person is adult or minor.  
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def check(self):
#         if(self.age<18):
#             print(self.name,"is Minor with the age being ",self.age)
#         else:
#             print(self.name,"is an Adult with the age being",self.age)
# p1=Person("Ayush",19)
# p1.check()
# p2=Person("Mayur",7)
# p2.check()

#HARD 

# Create a class Account with:

# balance
# account number

# Add methods:

# credit
# debit
# transfer money
# 14

# Create a class Student and:

# store marks in list
# calculate highest marks
# calculate average
# 15

# Create a class ShoppingCart:

# add items
# remove items
# calculate total bill
# 16

# Create a class Library:

# store books in list
# issue a book
# return a book
# 17

# Create a class ATM:

# check PIN
# withdraw cash
# deposit cash
# check balance
# 18

# Create a class Movie:

# movie name
# rating
# duration

# Add method:

# check if movie is hit (rating > 8)
# STATIC METHOD PRACTICE
# 19

# Create a class with:

# a static method that prints welcome message.
# 20

# Create a class MathUtils with static methods:

# square
# cube

# ABSTRACTION / REAL-WORLD THINKING
# 21

# Create a class Fan:

# state ON/OFF
# methods:
# turn on
# turn off
# 22

# Create a class Car:

# accelerate
# brake
# show speed