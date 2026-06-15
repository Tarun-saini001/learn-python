# Custom Validation Example
# def register(age):
#     if age<18:
#         raise Exception("Age must be 18 or above")
#     print("Register successfully")
    
# register(17)

#Creating custom exception
class InvalidAgeError(age):
    pass

age=-5

if age<0:
    raise InvalidAgeError("Age cannot be negative")