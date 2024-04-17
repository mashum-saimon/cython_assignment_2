# Write a Python function to find all duplicate elements in a list and return them in a new list.
# List = [1, 2, 3, 2, 4, 5, 4, 6]
def duplicate_ele(my_list):
    ans_list = []
    check={}
    for num in my_list:
        if num in check:
            check[num] += 1
        else:
            check[num] = 1
    for num in check:
        if check[num] > 1:
            ans_list.append(num)
    return ans_list
print(duplicate_ele([1, 2, 3, 2, 4, 5, 4, 6] ))