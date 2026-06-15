try:
    num1=10
    num2=0
    print(num1/num2)
   
except:
    print("cannot divide by 0")    
    
  
# Catch specific exceptions

try:
    print(10/0)
    
except ZeroDivisionError:
        print("cannot divide by 0")
        

#------------valeError
try:
    age = int("hello")

except ValueError:
    print("Invalid number")        
    
    
#-----------Multiple Exceptions
 
# try:
#     num = int(input("Enter number: "))
#     print(10 / num)

# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")   
    
 
#----------Exception Object (You can access the actual error message.)
# try:
#     print(10 / 0)

# except ZeroDivisionError as e:
#     print(e)    
    
#---------else Block (Runs only if no exception occurs.)

# try:
#     num = 10

#     print(num)

# except:
#     print("Error")

# else:
#     print("Everything worked")    
    
    
#----------finally Block (Runs always, whether an exception occurs or not)
try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Cleanup")    