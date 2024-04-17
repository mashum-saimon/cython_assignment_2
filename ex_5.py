# Write a Python function to check if a given string is a palindrome or not.
# String = "A man, a plan, a canal, Panama"
s= "A man, a plan, a canal, Panama"
def palindrome(stp):
    revstr=(stp[::-1])
    if revstr==stp:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome(s)
