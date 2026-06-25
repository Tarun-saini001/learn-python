# Adding Conditions
# [expression for item in iterable if condition]

numbers=[1,2,3,4,5,6]
even=[num for num in numbers if num%2==0]

print(even)

odd=[num for num in numbers if num%2!=0]

print(odd)

# Strings Longer Than 4 Characters
words = ["apple", "cat", "banana", "dog"]
result=[word for word in words if len(word)>4]
print(result)


# Conditional Expression (if-else)
# Syntax: [value_if_true if condition else value_if_false for item in iterable]

numbers=[1,2,3,4,5,6,7,8]
result=["even" if num%2==0 else "odd"
        for num in numbers]
print(result)


numbers=[-1,2,3,-4,-5]
result=["negative" if num<0 else "positive"
        for num in numbers]
print(result)