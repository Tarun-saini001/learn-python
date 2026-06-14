age = "22"

# age+10  (Python will give an error because you're trying to add an integer to a string.)


age = int("22") #Type conver(cast)
print(age + 10)

# Why Type Casting Is Needed
age = input("Enter your age: ")
print(type(age)) #Even though the user typed a number, input() always returns a string.


# To use it as a number:
age = int(input("Enter age: "))
print(type(age))