#SET- set stores unique values.

number= {1,2,2,3,3,4,5,6}

# duplicate removal
print(number)

#addition
number.add(7)
print(number)

#removal
number.remove(2)
print(number)

#check existence
if 7 in number:
    print("Found")

# Why sets are powerfull? suppose:

emails=[
     "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com"
]

unique_mails=set(emails)
print(unique_mails)

#------ Set Operations --------

# Union
a={1,2,3}; b={3,4,5}
print(a | b)

#Difference
print(a-b)
