def is_palindrome(string):
    reverse=""
    for char in string:
        reverse=char+reverse
    return reverse==string
    
print(is_palindrome("tat"))        