# DAY - 5 

#EASY

#Q1.Create a list of 5 numbers and print: first element and last element
# list = [1,2,3,4,5]
# print("First element = ",list[0])
# print("Last element = ",len(list))  

#Q2.Create a list of names and print the length of the list.
# list = ["Ayush","Yash","Gauri","Ravi","Abhi"]
# print("Length of the list is : ",len(list)) 

#Q3.Create a list and: change the second element , print updated list
# list = ["Ayush",2,"Yash",5]
# print("Before update : ",list)
# list[1]=1
# print("After update : ",list) 

#Q4.Take a list of numbers and print a slice from index 1 to 3.
# list = ["Ayush",2,"Yash",5,"Abhi",7]  
# print(list[1:4]) 

#Q5.Create a list and: # append a new element and print the updated list
# list = ["Ayush",2,"Yash",5]
# print("List before append : ",list)
# list.append("yashvi")
# print("List after append : ",list)

#Q6.Create a list of 5 numbers and: remove the last element using pop()
# list = ["Ayush",2,"Yash",5]
# list.pop()
# print(list) 

#MEDIUM

#Q7.Create a list of numbers and: sort it in ascending / descending order
# list = [ 3,1,6,8,2,0,5]
# print("Actual list : ",list)
# list.sort()
# print("Ascending order : ",list)
# list.sort(reverse="True")
# print("Descending order : ",list)  

#Q8.Create a list of numbers and: find the maximum/minimum
# list = [ 3,1,6,8,2,0,5]
# print("Minimum : ",min(list))
# print("Maximum : ",max(list)) 

#Q9.Create a list and: insert a value at index 2
# list = [4,8,10,16]
# list.insert(2,12) 
# print("List after insert : ",list)

#Q10.Create a list and: reverse it using .reverse()
# list = [1,2,3,4]
# list.reverse()
# print("Reversed list ",list) 

#Q11.Take a list of numbers and count how many times a number appears
# list = [1,2,1,3,4,1,5,1,6,7,1]
# print("1 appeared : ",list.count(1),"times") 

#HARD

#Q12.Take a list of numbers and: calculate the sum of all elements 
# list = [1,2,3,4,5,6]
# print(sum(list)) 

#Q13.Take a list and:find the second largest number
# lst = [10, 5, 8, 20, 15]
# lst.sort() 
# second_largest = lst[-2]
# print("Second largest:", second_largest)

#Q14.Take a list and: remove all duplicate elements
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique_lst = set(lst) 
# print("After removing duplicates:", unique_lst)

#Q15.Take a list and: check whether it is a palindrome
# lst = [1, 2, 3, 2, 1] 
# if lst == lst[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome") 

#Q16.Take two lists and:merge them into one list
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged = list1 + list2
# print("Merged list:", merged)
