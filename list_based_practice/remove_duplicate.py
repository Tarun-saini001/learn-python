def unique(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
            
    return result

print(unique([1,1,1,2,3,3,4]))  