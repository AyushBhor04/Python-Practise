#DAY-11

#EASY

#Q1.Write a function to take two numbers and return their sum
# def sum(a,b):
#     print(a+b)
# x=int(input("enter a value : "))
# y=int(input("enter a value : "))
# print(sum(x,y)) 

#Q2.Write a function that prints "Hello, <name>" takes name as input
# def show(abc):
#     print("Hello ",abc)
# xyz=input("Enter your name : ")
# show(xyz) 

#Q3.Write a function to return the square of a number
# def square(a):
#     print(a*a)
# x=int(input("Enter any number : "))
# square(x)  

#Q4.Write a function with default parameters multiply two numbers , default values should be used if no arguments passed
# def mul(a=7,b=8):
#     print(a*b)
# mul() 
# x=int(input("Enter any number : "))
# y=int(input("Enter any number : "))
# mul(x,y)

#Q5.Write a function that takes a list returns its length (don’t use len() inside print directly)
# def get_length(lst):
#     count = 0
#     for _ in lst:
#         count += 1
#     return count
# nums = [1, 2, 3, 4, 5]
# print("Length:", get_length(nums))

#Q6.Write a function that takes a list prints all elements in one line 
# def print_list(lst):
#     for item in lst:
#         print(item, end=" ")
# nums = [1, 2, 3, 4, 5]
# print_list(nums)

#MEDIUM

#Q7.Write a function to find maximum of three numbers
# def max(a,b,c):
#     if(a>b and a>c):
#         print(a,"is the greatest")
#     elif(b>a and b>c):
#         print(b,"is the greatest")
#     else:
#         print(c,"is the greatest")
# x=int(input("Enter a number : "))
# y=int(input("Enter a number : "))
# z=int(input("Enter a number : "))
# max(x,y,z) 

#Q8.Write a function to check whether a number is even or odd return result 
# def parity(num):
#     if(num%2==0):
#         print("Even")
#     else:
#         print("Odd")
# a=int(input("Enter any number : "))
# parity(a) 

#Q9.Write a function to calculate factorial using loop
# def fact(n):
#     prod = 1
#     for i in range(1, n + 1):
#         prod = prod * i
#     return prod
# a = int(input("Enter any number: "))
# xyz = fact(a)
# print(xyz)

#Q10.Write a function to count vowels in a string
# def count_vowels(s):
#     count = 0
#     for ch in s.lower():
#         if ch in "aeiou":
#             count += 1
#     return count
# text = input("Enter a string: ")
# print("Vowel count:", count_vowels(text))

#Q11.Write a function to take a list return sum of all elements
# def list_sum(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total
# nums = [1, 2, 3, 4, 5]
# print("Sum:", list_sum(nums))

#Q12.Write a function to check if a number is prime 
# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("Prime")
# else:
#     print("Not Prime")

#HARD

#Q13.Write a function to find second largest number in a list
# def second_largest(lst):
#     largest = second = float('-inf')
#     for num in lst:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num
#     if second == float('-inf'):
#         return "No second largest element"
#     return second
# print(second_largest([4, 7, 2, 9, 5]))

#Q14.Write a function to remove duplicates from a list
# def remove_duplicates(lst):
#     result = []
#     for num in lst:
#         if num not in result:
#             result.append(num)
#     return result
# print(remove_duplicates([1, 2, 2, 3, 1, 4]))

#Q15.Write a function to return reversed version of a list
# def reverse_list(lst):
#     rev = []
#     for i in range(len(lst) - 1, -1, -1):
#         rev.append(lst[i])
#     return rev
# print(reverse_list([1, 2, 3, 4]))

#Q16.Write a function to count frequency of elements in a list (use dictionary)
# def frequency(lst):
#     freq = {}
#     for num in lst:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
#     return freq
# print(frequency([1, 2, 2, 3, 1, 4]))

#Q17.Write a function to check if a string is palindrome 
# def is_palindrome(s):
#     return s == s[::-1]
# text = input("Enter a string: ")
# if is_palindrome(text):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#RECURSION 

#Q18.Write a recursive function to print numbers from 1 to N
# def print_1_to_n(n):
#     if n == 0:
#         return
#     print_1_to_n(n - 1)
#     print(n)
# print_1_to_n(5) 

#Q19.Write a recursive function to calculate factorial
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)
# print(fact(5))

#Q20.Write a recursive function to calculate sum of first N numbers
# def sum_n(n):
#     if n == 1:
#         return 1
#     return n + sum_n(n - 1)
# print(sum_n(5)) 

#Q21.Write a recursive function to find nth Fibonacci number
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(6))

#Q22.Write a recursive function to reverse a string
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]
# print(reverse_string("hello"))

#Q23.Write a recursive function to count digits in a number 
# def count_digits(n):
#     n = abs(n)
#     if n < 10:
#         return 1
#     return 1 + count_digits(n // 10)
# print(count_digits(12345))