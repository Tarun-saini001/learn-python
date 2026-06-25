square={x: x*x for x in range(5)}
print(square)

# word length
names=["python","java","javascript"]
result={name:len(name) for name in names}
print(result)

# Conditional example
numbers=[1,2,3,4,5,6,7]
result={
    num: num*num
    for num in numbers
    if num%2==0
        }
print(result)