#DAY-6

#EASY

#Q1.Create a tuple of 5 numbers and print:# first and last element
# tup=(1,2,3,4,5)
# print("First element : ",tup[0]) 
# print("Last element : ",len(tup))  

#Q2.Create a tuple and print its length.
# tup=(1,2,3,4) 
# print("Length of the tuple : ",len(tup))  

#Q3.Create a tuple with a single element and print its type.
# tup=(1,)
# print(type(tup)) 

#Q4.Create a tuple and print a slice from index 1 to 3.
# tup = (1,4,5,2,5,7,8,3,4,6,0)
# print(tup[1:4]) 

#Q5.Create a tuple and: find index of a given element count how many times it appears
# tup=(1,2,3,4,1,5,1,6,3,7,1,1,6,7,8,1,9)
# print("Index of element 5 is : ",tup.index(5))
# print("Element 1 occurs : ",tup.count(1)) 

#Q6.Create a tuple and try to modify an element , observe and explain what happens.
# tup=(1,2,3,4,1,5,1,6,3,7,1,1,6,7,8,1,9)
# tup[3]=7
# print(tup) 

#MEDIUM

#Q7.Take 3 inputs from user and store them in a list.
# a = input("Enter name : ")
# b = input("Enter name : ")
# c = input("Enter name : ")
# list=[a,b,c] 
# print(list)  

#Q8.Take 5 numbers from user and store them in a tuple.
# a = input("Enter name : ")
# b = input("Enter name : ")
# c = input("Enter name : ")
# d = input("Enter name : ")
# e = input("Enter name : ")
# tup=(a,b,c,d,e)
# print(tup) 

#Q9.Given a tuple: (1, 2, 3, 2, 4, 2) Count how many times 2 appears.
# tup=(1, 2, 3, 2, 4, 2)
# print("Element 1 appears : ",tup.count(2),"times")

#Q10.Convert a tuple into a list and:sort it in ascending order 
# tup = (6, 2, 1, 3, 5 , 4)
# lst = list(tup)
# print("Tuple:", tup)
# print("Converted List:", lst) 
# lst.sort()
# print("Sorted list : ", lst) 

#Q11.Create a list and:convert it into a tuple
# lst = [2,4,1,3,5]
# tup=tuple(lst)
# print("List : ",lst)
# print("Tuple : ",tup)

#Q12.Take a list and check whether it is a palindrome.
# lst=[1,2,3,2,1] 
# if(lst==lst[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome") 

#HARD

#Q13.Take a tuple of numbers and find the maximum value
# tup=(2,4,1,5,6,3)
# print("Max element : ",max(tup))   

#Q14.Take a tuple convert it to list remove duplicates convert back to tuple
# tup=(2,4,1,5,6,3,2,3,5,9,11,3,44)
# lst=list(tup)
# lst_1=set(lst)
# tupl=tuple(lst_1)
# print(tupl,type(tupl))  

#Q15.Mqke a list of numbers and:create a new list containing only unique elements
# lst=(2,4,1,5,6,3,2,3,5,9,11,3,44)
# lst_1=set(lst)
# print(lst_1) 

#Q16.Take a list of grades:["A", "B", "A", "C", "B", "A"] and count how many students got each grade.
grades=["A", "B", "A", "C", "B", "A"]
print("A :",grades.count("A"))
print("B :",grades.count("B"))
print("C :",grades.count("C"))