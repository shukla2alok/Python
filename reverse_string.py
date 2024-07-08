# Write a program to reverse the string

def reverse_string(s):
    return s[::-1]

s = input("Enter the String: ")
print(s)
print("Reverse String is: ", reverse_string(s))