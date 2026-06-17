def is_palindrome(num):
    if num < 0:
        return False

    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse

print(is_palindrome(1221))