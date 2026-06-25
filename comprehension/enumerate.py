# enumerate() is a built-in Python function that adds a counter (index) to an iterable and returns both the index and the value during iteration.

# provlem without enumerate
numbers=[10,20,30]
print("Without enumerate")
for i in range(len(numbers)):
    print(i, numbers[i])
    
# with enumerate
print("With enumerate")
for index,value in enumerate(numbers):
    print(index,value)
    
    
# How enumerate Works

# Think of it as converting:

# [10,20,30]

# into:

# [
#     (0,10),
#     (1,20),
#     (2,30)
# ]    
    
# Then python unpacks : index, value from each tuple   

for item in enumerate(numbers): #visualize it
    print(item) 
    

#starting from different index
name=["Tarun","Sahil","Nitish"]
for index,value in enumerate(name,start=1):
    print(index,value)    
    
    
#Real DSA example
nums=[5,10,6]
for i,num in enumerate(nums):
    if num==10:
        print("found at",i)    