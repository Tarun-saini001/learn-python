def count_digit(num):
    if num==0:
        return 1
    
    
    num=abs(num)
    
    count=0
    
    while num>0:
        count+=1
        num//=10
        
    return count

print(count_digit(12345))
print(count_digit(-1123))
print(count_digit(0))
    