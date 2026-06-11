# Identity Operators Checks, Are two variables referring to the same object in memory?

a=[1,2]

b=a #Python does not create a new list. It makes b point to the same list.
print(a is b) #checks whether a and b refer to the same object, which is True.

a.append(3)

print(a) 
print(b) #Changing the list through a also affects b because they reference the same object.

#If you want a separate copy

c=a.copy()
print(c is a) #false

print(c is not a) #true
