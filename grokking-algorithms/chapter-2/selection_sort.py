def find_smallest(arr: list) -> int:
    """
    :param arr: An array of integers in question
    :return int: the index of the smallest element in the array
    """

    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


my_arr = [1, 5, 5, 8, 2, 0]
print(find_smallest(my_arr))

"""
Considering 1,5,5,8,2,0

Initially smallest=1, smallest_index=0

for the for loop
when i=1
we compare if 5<1, and it's false

when i=2
same result

i=3
we compare if 8<1 and it's false, so smallest and smallest_index remains 1 and 0 respectively

i=4
we comapre if 2<1 and it's fasle

i=5
we compare if 0<1 and it's true
so we set smallest=0 and smallest index=5
then return 0
"""


def selection_sort(arr: list) -> list:
    """
    :param arr - list of items to sort
    :return list - sorted lists
    """
    new_arr = []
    copied_arr = list(arr)  # copy array before mutating

    for _ in  range(len(copied_arr)):
        smallest = find_smallest(copied_arr) # returns index of smallest value
        smallest_value=copied_arr.pop(smallest) #returns the value at the popped index
        new_arr.append(smallest_value)

    return new_arr

print(selection_sort(my_arr))
