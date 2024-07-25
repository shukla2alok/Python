# write a program to check palindrome


def palindrome(s):
    return s == s[::-1]

s = input("Enter the String: ")
print(s)
if(palindrome(s)):
    print(s, "is palindrome")
else:
    print(s, "is not palindrome.")