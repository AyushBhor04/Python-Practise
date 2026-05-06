#DAY-7

#EASY

#Q1.Create a dictionary with:name age city and print all values.
# dict = {
#     "name":"Ayush",
#     "age":24,
#     "city":"Mumbai"
# }
# print(dict) 
# print(type(dict))

#Q2.Create a dictionary and: print value using key try accessing a non-existing key (observe behavior)
# dict = {
#     "name":"Ayush",
#     "age":24,
#     "city":"Mumbai"
# }
# print(dict["name"])
# print(dict["age"])
# print(dict["city"])
# print(dict["Location"]) 

#Q3.Create a dictionary and: update one value,add a new key-value pair
# dict = {
#     "name":"Ayush",
#     "age":24,
#     "city":"Mumbai"
# }
# dict["name"]="Yash"
# print(dict)
# dict["dob"]="4Th March 2002" 
# print(dict) 

#Q4.Create an empty dictionary and add 3 key-value pairs dynamically
# Create empty dictionary
# my_dict = {}
# my_dict["name"] = "Ayush"
# my_dict["age"] = 23
# my_dict["course"] = "M.Tech"
# print(my_dict)

#Q5.Create a dictionary and print: all keys,all values
# dict = {
#     "name":"Ayush",
#     "age":24,
#     "city":"Mumbai"
# }
# print("Key : ",dict.keys())
# print("Values : ",dict.values()) 

#Q6.Create a dictionary and print the number of key-value pairs.
# my_dict = {
#     "name": "Ayush",
#     "age": 23,
#     "course": "M.Tech"
# }
# print("Number of pairs:", len(my_dict))

#MEDIUM

#Q7.Create a dictionary of student marks and print all subjects and marks
# student={
#     "marks":[99,95,100,45],
#     "subject":["Maths","Chem","Bio","Stats"] 
# }
# print("Marks :",student["marks"])
# print("Subject :",student["subject"])  

#Q8.Create a dictionary and check if a key exists using .get()
# info = {
#     "name": "Ayush",
#     "age": 23,
#     "course": "M.Tech"
# }
# key = "age"
# if info.get(key) is not None:
#     print("Key exists")
# else:
#     print("Key does not exist")

#Q9.Create a dictionary and: convert keys into a list AND convert values into a list
# info = {
#     "name": "Ayush",
#     "age": 23,
#     "course": "M.Tech"
# }
# keys_list = list(info.keys())
# values_list = list(info.values())
# print("Keys:", keys_list)
# print("Values:", values_list)

#Q10.Create two dictionaries and merge them using .update()
# dict1 = {
#     "name": "Ayush",
#     "age": 23
# }
# dict2 = {
#     "course": "M.Tech",
#     "city": "Mumbai"
# }
# dict1.update(dict2)
# print(dict1)

#Q11.Create a nested dictionary for a student: name,subjects → (phy, chem, math marks) # Print the marks of one subject.
# student = {
#     "name": "Ayush",
#     "subjects": {
#         "phy": 85,
#         "chem": 90,
#         "math": 95
#     }
# }
# print("Chemistry marks:", student["subjects"]["chem"])

#Q12.Create a dictionary and print all key-value pairs using .items()
# info = {
#     "name": "Ayush",
#     "age": 23,
#     "course": "M.Tech"
# }
# for key, value in info.items():
#     print(key, ":", value)

#Q13.Create a dictionary and: change multiple values using another dictionary
# info = {
#     "name": "Ayush",
#     "age": 23,
#     "city": "Mumbai"
# }
# update_data = {
#     "age": 24,
#     "city": "Pune"
# }
# info.update(update_data)
# print(info)

#HARD

#Q14.Take input of 3 subjects and marks from user and store in a dictionary.
# marks = {}
# for i in range(3):
#     subject = input("Enter subject name: ")
#     score = int(input("Enter marks: "))
#     marks[subject] = score
# print("Marks dictionary:", marks)

#Q15.Create a dictionary and: find the key with the maximum value
# marks = {
#     "phy": 85,
#     "chem": 90,
#     "math": 95
# }
# max_key = max(marks, key=marks.get)
# print("Subject with highest marks:", max_key)

#Q16.Create a dictionary and:count how many values are greater than a given number
# marks = {
#     "phy": 85,
#     "chem": 90,
#     "math": 95
# }
# threshold = int(input("Enter number: "))
# count = 0
# for value in marks.values():
#     if value > threshold:
#         count += 1
# print("Count:", count)

#Q17.Create a dictionary and:remove a key (without using built-in pop directly if possible)
# info = {
#     "name": "Ayush",
#     "age": 23,
#     "city": "Mumbai"
# }
# key_to_remove = "age"
# if key_to_remove in info:
#     del info[key_to_remove]
# print(info)

#Q18.Create a dictionary and swap keys and values. Example:# {"a":1, "b":2} → {1:"a", 2:"b"}
# data = {"a": 1, "b": 2, "c": 3}
# swapped = {}
# for key, value in data.items():
#     swapped[value] = key
# print(swapped)

#Q19.Create a dictionary of words and count frequency of each character in a string # Example "apple" → {"a":1, "p":2, "l":1, "e":1}
# word = "apple"
# freq = {}
# for char in word:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# print(freq)

#Q20.Create a nested dictionary and: # print all inner keys and values
# students = {
#     "student1": {
#         "phy": 85,
#         "chem": 90
#     },
#     "student2": {
#         "phy": 78,
#         "chem": 88
#     }
# }
# for student, subjects in students.items():
#     print(student)
    
#     for subject, marks in subjects.items():
#         print(" ", subject, ":", marks)