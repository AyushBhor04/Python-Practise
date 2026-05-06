#DAY-3 

#EASY

#Q1.Create a string and print it using: # double quotes # single quotes # triple quotes
# str_1="Ayush Bhor"
# str_2='Ayush Bhor'
# str_3='''Ayush Bhor'''
# print(str_1)
# print(str_2) 
# print(str_3)

#Q2.Write a string that contains an apostrophe (') and print it correctly.
# str_1="Ayush's Bhor"
# print(str_1) 

#Q3.Print a string in two lines using \n.
# str_1="My name is Ayush\nI am 24 year old" 
# print(str_1) 
 
#Q4.Create two strings:
# "Hello" # "World"
# Concatenate them and print the result.
# str_1="Hello"
# str_2="World"
# str_3=str_1 + str_2 
# print(str_3) 

#Q5.Create a string with your first name and print its length.
# name=input("Enter your name : ")
# print(name)
# print(len(name))  

#Q6.Create two strings:
# first name # last name
# Concatenate them with a space in between and print the full name.
# str_1="Ayush"
# str_2="Bhor"
# str_3=str_1+" "+str_2
# print(len(str_3)) 

#Q7.Given a string: # "Python"
# Print: # first character # last character 
# str_1="Python"
# print(str_1[0]) 
# print(str_1[-1]) 

#MEDIUM

#Q8.Given a string:"Apna College"
# Print characters from index 1 to 4 using slicing.
# str = "Apna College"
# print(str[1:5]) 

#Q9.Given a string:# "Programming"
# Print everything from index 3 to the end.
# str = "Programming"
# print(str[3:len(str)])  

#Q10.Given a string: "HelloWorld"
# Print the last 3 characters using negative slicing.
# str="Helloworld" 
# print(str[-3:len(str)])

#Q11.Write a program to check if a string ends with a given word.
# str="Hello Ayush"
# print(str.endswith("Ayus")) 
# print(str.endswith("Ayush")) 

#Q12.Take a string and: # capitalize it  # Replace all occurrences of "a" with "o" in a string.
# Replace a word in a sentence with another word.
# Find the first occurrence index of a character in a string.
# Count how many times a character appears in a string.
# str="hello ayush" 
# print(str.capitalize()) 
# print(str.replace("a","o")) 
# print(str.replace("ayush","bitch")) 
# print(str.find("y"))
# print(str.count("h")) 

#HARD

#Q13.Take the user’s name as input and print the length of the name.
# str=input("Enter your name : ")
# print(str)
# print(len(str)) 

#Q14.Given a string:"I love Python programming"
# Find the index of the word "Python".
# str="I love Python programming"
# print(str.find("Python"))

#Q15.Write a program to count the number of times "@" appears in a string.
# str="@@ayush@@"
# print(str.count("@")) 

#Q16.Write a program that takes a string and prints: first 3 characters , last 3 characters .
# str=input("Enter a string : ") 
# print(str[0:3])
# print(str[-3:len(str)]) 

#Q17.Write a program to check whether a given character exists in a string using .find().
# str="Ayush"
# print(str.find("A")) 

#Q18.Create a variable light and: # print "Stop" if red # print "Look" if yellow # print "Go" if green
# Extend the above program to print:Light is broken if none of the conditions match.
# Take input from the user for traffic light color and print the appropriate action.
# color=input("Enter any color : ")
# if(color=="Red"):
#     print("Stop")
# elif(color=="Yellow"):
#     print("Get Ready")
# elif(color=="Green"):
#     print("Go")
# else:
#     print("The Light is broken") 

#Q19.Take a number from the user and check whether it is: # greater than 10 or less than or equal to 10
# num=int(input("Enter any number : ")) 
# if(num>10 or num<10):
#     if(num>10):
#         print("Greater than 10")
#     else:
#         print("Less than 10")
# else:
#     print("Equal to 10") 

#Q20.Take a number and check whether it is positive or negative.
# num=int(input("Enter any number : ")) 
# if(num>0):
#     print("Positive") 
# else:
#     print("Negative") 

#Q21.Take two numbers and print which one is greater.
# a=int(input("Enter any number : "))
# b=int(input("Enter any number : "))
# if(a>b):
#     print(a)
# else:
#     print(b) 

#Q22.Take a string and count how many times a specific character appears (user input).
# str=input("Enter any string : ")
# val=input("ENter the character to be checked : ")
# print(str.count(val)) 

#Q23.Take a string and replace all spaces with underscores _.
# str=input("Enter any string : ")
# print(str.replace(" ","_"))