def factorial(num):
    if num<0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    
    for i in range(1, num+1):
        result *=i
        
    return result

print(factorial(5))    
print(factorial(-5))    


# Using recursion
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

print(factorial(5))