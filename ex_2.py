# Write a Python function to reverse the order of words in a given string - "Hello World"
str="Hello World"
words=str.split(" ")
words=words[-1::-1]
output=' '.join(words)
print(output)


