#Ask user for their name 
name = input("What is your name? ")

#Say hello to user
print("hello,", end="")
print(name)

#Remove whitespace form string
print("hello,", name.strip())
 
#Capitalizing user's string
print("hello,", name.capitalize())
#Uppercase user's strings
print("hello,", name.title())

#Escape keyword
print("hello, \"David\"")

#using the split function
print(name.split())

#Combimation of some functions
print("hello,", name.strip().title().split())