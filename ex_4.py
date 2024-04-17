# Write a Python function to count the number of vowels and consonants in a given string "Hello
# World"
s="Hello World"
def count(stp):
    vowels_count=0
    consonant_count=0
    vowels='AEIOUaeiou'
    for i in stp:
        if i in vowels:
            vowels_count+=1
        elif i !=' ':
            consonant_count+=1
    print("vowels :",vowels_count)
    print("consonant :",consonant_count)
count(s)



