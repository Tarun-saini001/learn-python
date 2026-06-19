def reverse_str(string):
    
    reverse=""
    for str in string:
        reverse= str+reverse
        
    return reverse
print(reverse_str("Tarun"))


# Indexed based solution

def reverse_str(string):
    
    reverse=""
    for i in range(len(string)-1, -1,-1):  #range(start, stop, step)
        reverse+=string[i]
        
    return reverse

print(reverse_str("saini"))    