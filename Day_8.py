#DAY-8

#EASY

#Q1.Create a set with duplicate values and print it , Observe what happens.
# sett={1,2,2,3,43,2,2,1,3,4,45,5,3,3,9}
# print(sett) 

#Q2.Create an empty set and print its type.
# sett={ }
# print(type(sett))

#Q3.Create a set and:add 3 different elements , print the set
# sett={}
# sett=set()
# sett.add("Ayush")
# sett.add("Yash")
# sett.add("Lobo")
# print(sett) 

#Q4.Create a set and:remove an element print updated set
# sett={1,2,3,4}
# sett.pop()
# print(sett) 

#Q5.Create a set and print its length
# sett={1,2,3,4}
# print(len(sett))  

#Q6.Create a set and clear all elements , print the set .
# sett={1 ,2 , 3}
# sett.clear() 
# print(sett) 

#MEDIUM

#Q7.Create a set of numbers and check if a given number exists in the set
# numbers = {1, 2, 3, 4, 5}
# num = int(input("Enter a number to check: "))
# if num in numbers:
#     print("Number exists in the set")
# else:
#     print("Number does not exist in the set")

#Q8.Create two sets:{1, 2, 3}{2, 3, 4} , find union and intersection
# s1={1,2,3}
# s2={2,3,4}
# print(s1.intersection(s2))
# print(s1.union(s2))

#Q9.Take a list with duplicate elements , convert it into a set  print unique values
# l1=[1,2,1,4,5,64,7,8,9,2,3]
# sett=set(l1)
# print(sett) 

#Q10.Create a set and pop 2 elements observe behavior
# sett={1,2,31,7}
# sett.pop()
# sett.pop()
# print(sett) 

#Q11.Take a sentence and count number of unique words using a set
# str={"Ayush","Yash","Ayush","Sasha"}
# print(len(str)) 

#Q12.Take a list of numbers and find how many unique numbers are present
# sett={1,33,2,1,23,4,4,2}
# print(len(sett)) 

#HARD

#Q13.Take two lists and find common elements using sets
# l1=[1,2,3,4]
# l2=[2,4,6]
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))

#Q14.Take two lists and find elements that are present in one list but not in the other
# l1=[1,2,3,4]
# l2=[2,4,6]
# s1=set(l1)
# s2=set(l2)
# print(s1.difference(s2))

#Q15.Take a list and remove duplicates while maintaining original order (Hint: use set carefully)
# lst = [1, 2, 3, 2, 4, 1, 5]
# seen = set()
# result = []
# for num in lst:
#     if num not in seen:
#         result.append(num)
#         seen.add(num)
# print("Original list:", lst)
# print("After removing duplicates:", result)

#Q16.Take a list of numbers and check if all elements are unique
# lst = [1, 2, 3, 4, 5]
# if len(lst) == len(set(lst)):
#     print("All elements are unique")
# else:
#     print("Duplicates exist")

#Q17.Take a list and find the first duplicate element
# lst = [1, 2, 3, 2, 4, 5]
# seen = set()
# for num in lst:
#     if num in seen:
#         print("First duplicate:", num)
#         break
#     seen.add(num)
# else:
#     print("No duplicates found")

#Q18.Create a set and store both 9 and 9.0 as separate values
# values = {
#     ("int", 9),
#     ("float", 9.0)
# }
# print(values)