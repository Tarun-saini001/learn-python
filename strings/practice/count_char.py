def count_char(string):
    
    count=0
    for char in string:
        if char !=" ":
            count+=1
    return count

print(count_char("Hello   "))    