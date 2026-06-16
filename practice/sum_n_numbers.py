def sum(*numbers):
    total=0
    for n in  numbers:
        total+=n
    return total

print(sum(1,2,-3,0,0,4,5))

# #Index based
# def sum_numbers(*numbers):
#     total = 0

#     for i in range(len(numbers)):
#         total += numbers[i]

#     return total

# print(sum_numbers(1, 2, 3, 4))