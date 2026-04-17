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
my_dict = {
    "name": "Ayush",
    "age": 23,
    "course": "M.Tech"
}


# Create a dictionary and:

# convert keys into a list
# convert values into a list
# 10

# Create two dictionaries and:

# merge them using .update()
# 11

# Create a nested dictionary for a student:

# name
# subjects → (phy, chem, math marks)
# Print the marks of one subject.
# 12

# Create a dictionary and:

# print all key-value pairs using .items()
# 13

# Create a dictionary and:

# change multiple values using another dictionary