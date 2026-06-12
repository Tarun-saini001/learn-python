#Old Style (Not Recommended)
name = "Tarun"
print("Hello",name)

#f-Strings (Recommended)
name= "Tarun"
age=21
print(f"My name is {name} and I am {age}")

#Escape Characters
print("Hello\nworld") #Next line
print("Hello\tworld") #Tab
print("He said \"Hello\"")#Quotes Inside String


#Loop Through String
name= "Tarun"

for ch in name:
    print(ch.upper())
    


# Important Interview Question
# Why Are Strings Immutable?

# Benefits:

# Better performance
# Safer memory management
# Hashable (can be dictionary keys)    