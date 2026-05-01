#DAY-10

#EASY

#Q1.Print all elements of a list using a for loop.
# lis=[2,3,4,6,8,9,26,5,7]
# for el in lis:
#     print(el)

#Q2.Print all characters of a string one by one.
# str="Ayush Bhor"
# for ch in str:
#     print(ch) 

#Q3.Print numbers from 1 to N using range().
# n = int(input("Enter any value : "))
# for i in range(n+1):
#     print(i) 

#Q4.Print numbers from N to 1 using range().
# n = int(input("Enter any value : "))
# for i in range(n,0,-1):
#      print(i) 

#Q5.Print all even numbers from 1 to 50 using range().
# seq=range(51)
# for i in seq:
#     if(i%2==0):
#         print(i)

#Q6.Print multiplication table of a number using for loop.
# n = int(input("Enter any value : "))
# for i in range(11):
#     print(i*n) 

#MEDIUM

#Q7.Take a list and print only elements greater than 10
# num = [2,13,66,7,8,90,7,5,43,22,12,0,8]
# for el in num :
#     if(el>10):
#         print(el) 

#Q8.Take a string and count number of vowels
# str="Ayush Bhor is m.tech student"
# count = 0
# for ch in str:
#     if(ch=="a","e","i","o","u"):
#         count = count + 1
# print("Number of vowel : ",count)

#Q9.Take a list and find sum of all elements
# num = [2,13,66,7,8,90,7,5,43,22,12,0,8]
# sum=0
# for el in num:
#     sum=sum+el 
# print("Sum of elements of the list are : ",sum)

#Q10.Take a tuple and search for an element and print its index
# tups=(2,13,66,7,8,90,7,5,43,22,12,0,8)
# x=int(input("Enter any number : "))
# idx=0
# for el in tups:
#     if(el==x):
#         print("Element at ",idx)
#     idx+=1

#Q11.Take a list and count how many elements are even and odd
# num = [2,13,66,7,8,90,7,5,43,22,12,0,8]
# even=0
# odd=0
# for i in num:
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("The count of even number is : ",even)
# print("The count of odd number is : ",odd)

#Q12.Print squares of numbers from 1 to N using for loop.
# N=int(input("Enter any number : "))
# for i in range(N+1):
#     print(i*i)

#Q13.Take a number and print its multiplication table and stop early if result exceeds 100 
# n=int(input("Enter any number : "))
# for i in range(11):
#     if(n*i>100):
#         break 
#     else:
#         print(n*i) 

#HARD

#Q14.Take a list and find largest and smallest element using loop
# num = [2,13,66,7,8,90,7,5,43,22,12,0,8]
# larg=0
# small=100000
# for el in num:
#     if(el>larg):
#         larg=el
#     elif(el<small):
#         small=el 
# print("Largest value : ",larg)
# print("Smallest value : ",small) 

#Q15.Take a list and find second largest element
# lst = [4, 7, 2, 9, 5]
# largest = second = float('-inf')
# for num in lst:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num
# if second == float('-inf'):
#     print("No second largest element")
# else:
#     print("Second largest:", second)

#Q16.Take a list and reverse it using loop (no slicing)
# lst = [1, 2, 3, 4, 5]
# rev = []
# for i in range(len(lst) - 1, -1, -1):
#     rev.append(lst[i])
# print("Reversed list:", rev)

#Q17.Take a list and remove duplicates using loop
# lst = [1, 2, 3, 2, 4, 1, 5]
# result = []
# for num in lst:
#     if num not in result:
#         result.append(num)
# print("After removing duplicates:", result)

#Q18.Take a number and check if it is prime using for loop
# num = int(input("Enter number: "))
# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

#Q19.Take a string and count frequency of each character
# s = input("Enter a string: ")
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)

#20.Take a list and print elements at even index positions
# num = [2,13,66,7,8,90,7,5,43,22,12,0,8]
# idx=0
# for el in num:
#     if(idx%2==0):
#         print(el)
#     idx+=1
