def count_char(string):
    
    count=0
    for char in string:
        if char !=" ":
            count+=1
    return count

print(count_char("Hello   "))    

#Count unique

def count_unique_chars(string):
    unique_chars=[]
    for char in string:
        if char != " " and char not in unique_chars:
            unique_chars.append(char)
            
    return len(unique_chars)  

print(count_unique_chars("aaaaabc"))     