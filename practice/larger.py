def large(a,b,c):
    if a==b==c:
        print("All numbers are equal")
        return
    if(a>=b and a>=c):
        print(f"A is larger: {a}")
        return
    elif (b>=a and b>=c):
        print(f"B is larger: {b}")
        return
    else:
        print(f"C is larger: {c}")
        
large(1,1,1)        
            
        