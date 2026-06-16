def is_even(num):
    if not isinstance(num,int):
        print("Please enter a integer.")
        return
    
    if(num%2==0):
        print("Even")
    else:
        print("Odd")    
        
is_even(-6.5)        