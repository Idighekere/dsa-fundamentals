def quick_sort(arr):
    """
    A function to sort an array using the quick sort algorithm
    :param arr
    return list - the sorted array

    """
    # base case
    if len(arr)<=1:
        return arr


    pivot = arr[0]

    less= [i for i in arr[1:] if i <pivot]
    greater= [i for i in arr[1:] if i >=pivot]

    return quick_sort(less)+[pivot]+quick_sort(greater)

arr_1=[3,2,5,4,1,1]

print(quick_sort(arr_1))
