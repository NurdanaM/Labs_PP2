def is_palindrome(word):
    if word == word[::-1]:
        return "Palindrome"
    else:
        return "Not"
    
word = "madam"
print(is_palindrome(word))