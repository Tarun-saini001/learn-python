# List comprehension is a short and Pythonic way to create lists.
# As a MERN developer, think of it as something similar to JavaScript's map() and filter().

# General Syntax
# ----[new_value for item in iterable]----
# Suppose you want a list of squares.

# traditional way
squares = []

for i in range(5):
    squares.append(i * i)

print(squares)

#using list comprehension
squares =[i*i for i in range(5)]
print(squares)


#Copy list
numbers=[1,2,3,4,6]
new_list=[num for num in numbers]
print(new_list)

#convert uppercase
names=["tarun","sahil"]
result=[name.upper() for name in names]
print(result)