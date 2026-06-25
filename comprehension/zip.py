# zip() is a built-in Python function that combines elements from two or more iterables into pairs (or tuples) based on their positions.

# without zip
names=["Tarun", "Rahul"]
ages=[20,23]
print("Without zip")
for i in range(len(names)):
    print(names[i],ages[i])
    
    
# with zip
print("With zip")
for name,age in zip(names,ages): #Cleaner and more Pythonic.
    print(name,age)   
    
 
# How zip Works

# Think of:

# zip(names, ages)

# as creating:

# [
#     ("Tarun", 22),
#     ("Rahul", 23)
# ]    

# Then Python unpacks: name, age  from each tuple.

for item in zip(names, ages): # Visualize It
    print(item)
    
    
# Multiple list    
names = ["Tarun", "Rahul"]
ages = [22, 23]
cities = ["Delhi", "Chandigarh"]

for name,age,city in zip(names,ages,cities):
    print(name,age,city)
    

# Create Dictionary Using zip()
names=["Tarun","Sahil"]
ages=[20,21]

result=dict(zip(names,ages))
print(result)    


# When To Use What?

# Use enumerate()- When you need: index + value
# Use zip()- When you need: multiple lists together