#DAY-9

#EASY

#Q1.Print numbers from 1 to N (user input).
# n = int(input("Enter any number : "))
# i = 1 
# while (i<=n):
#     print(i)
#     i+=1
# print("Numbers printed from 1 to",n)

#Q2.Print numbers from N to 1.
# n = int(input("Enter any number : "))
# N=n
# i = 1 
# while (n>=i):
#     print(n)
#     n-=1
# print("Numbers printed from",N, "to 1") 

#Q3.Print all even numbers from 1 to 50.
# i = 1 
# print("Even Number from 1 to 50")
# while(i<=50):
#     if(i%2==0):
#         print(i)
#     i+=1

#Q4.Print all odd numbers from 1 to 50.
# i = 1 
# print("Odd Number from 1 to 50")
# while(i<=50):
#     if(i%2!=0):
#         print(i)
#     i+=1

#Q5.Print the sum of numbers from 1 to N.
# sum = 0 
# i=1
# n=int(input("Enter any number n : "))
# while(i<=n):
#     sum=sum+i
#     i+=1
# print("Sum of 1st 5",n,"numbers is ",sum )

#Q6.Print the multiplication table of a number (same as yours, but formatted nicely).
# n=int(input("Enter any number : "))
# print("Multiplication table for ",n)
# i=1
# while(i<=10):
#     print(n,"* ",i,"= ",n*i)
#     i+=1

#MEDIUM

#Q7.Take a number and count number of digits
# num = int(input("Enter a number: "))
# count = 0
# num = abs(num)
# if num == 0:
#     count = 1
# else:
#     while num > 0:
#         count += 1
#         num //= 10
# print("Number of digits:", count)

#Q8.Reverse a number using loop Example:123 → 321
# num = int(input("Enter a number: "))
# rev = 0
# n = abs(num)
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# print("Reversed number:", rev)

#Q9.Check if a number is a palindrome using loop
# num = int(input("Enter a number: "))
# original = num
# rev = 0
# n = abs(num)
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# if num < 0:
#     rev = -rev
# if original == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Q10.Take a number and find sum of its digits
# num = int(input("Enter a number: "))
# total = 0
# n = abs(num)
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print("Sum of digits:", total)

#Q11.Print all numbers from 1 to N that are divisible by both 3 and 5
# i=1
# N=int(input("Enter any value n : "))
# print("All numbers divisible by both 3 and 5 in the range 1 to",N,"are :")
# while(i<=N):
#     if(i%3==0 and i%5==0):
#         print(i)
#     i+=1

#Q12.Take a list and print all elements using loop (no indexing shortcut)
# li=[2,4,5,8,4,2,1,14,4,57,246,52,4627,3]
# idx=0
# while(idx<=len(li)):
#     print(li[idx])
#     idx+=1

#Q13.Search for a number in a list and print index stop once found
# li=[2,4,5,8,4,2,1,14,4,57,246,52,4627,3]
# el=int(input(print("Enter the number to be found : ")))
# idx=0
# while(idx<=len(li)):
#     if(li[idx]==el):
#         print("Element found at index ",idx)
#         break
#     else:
#         idx+=1

#14.Count how many numbers in a list are even odd
# li=[2,4,5,8,4,2,1,14,4,57,246,52,4627,3]
# odd = 0
# even = 0 
# idx=0
# while(idx<len(li)):
#     if(li[idx]%2==0):
#         even+=1
#         idx+=1
#     else:
#         odd+=1
#         idx+=1
# print("Number of even numbers in the list : ",even)
# print("Number of odd numbers in the list : ",odd)

#HARD

#Q15.Take a number and check if it is prime
# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Not Prime")
# else:
#     is_prime = True
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")

#Q16.Print the factorial of a number
# num = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= num:
#     fact *= i
#     i += 1
# print("Factorial:", fact)

#Q17.Take a list and find the largest element manually (no max())
# lst = [4, 7, 2, 9, 5]
# largest = lst[0]
# for num in lst:
#     if num > largest:
#         largest = num
# print("Largest:", largest)

#Q18.Take a list and find the second largest number
# lst = [4, 7, 2, 9, 5]
# largest = second = float('-inf')
# for num in lst:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num
# print("Second largest:", second)

#Q19.Take a list and remove all occurrences of a given number
# lst = [1, 2, 3, 2, 4, 2, 5]
# x = int(input("Enter number to remove: "))
# result = []
# for num in lst:
#     if num != x:
#         result.append(num)
# print("Updated list:", result)

#Q20.Take a list and reverse it using loop (no slicing) 
# lst = [1, 2, 3, 4, 5]
# rev = []
# i = len(lst) - 1
# while i >= 0:
#     rev.append(lst[i])
#     i -= 1
# print("Reversed list:", rev)