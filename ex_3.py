# Given a list of n-1 integers from 1 to n, find the missing number in the list.
# List = [1, 2, 4, 6, 3, 7, 8] # Output: 5
input_list=[1, 2, 4, 6, 3, 7, 8]
for i in range(1,9):
    if not i in input_list:
        print(i)