# Write a Python function to remove the duplicates in-place from a sorted array and return the
# length of the new array/list without duplicates.
# List = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def remove_duplicates(list):
    empty_list=[]
    for element in list:
        if element not in empty_list:
            empty_list.append(element)
    return len(empty_list)
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
