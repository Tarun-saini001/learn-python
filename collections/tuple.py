#TUPLE- Tuple is an immutable list

# Why Use Tuple?

# When values should never change.

# Examples:

# DAYS = (
#     "Monday",
#     "Tuesday",
#     "Wednesday"
# )

coordinates=(4,8)

#access 
print(coordinates[1])

# #can not modify
# coordinates[0]=2
# print(coordinates)


#tuple packing
point = 1,2
print(type(point))
print(point)

#tuple unpacking
student=("Tarun",21,"Radaur")
name, age, address = student
print(name)
print(age)
print(address)