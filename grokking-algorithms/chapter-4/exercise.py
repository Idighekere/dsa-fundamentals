##======= Exercise 4.1

def sum(arr):
    """
    A function to find the sum of an array 
    :param arr - an array to sum
    :return int
    """

    total=0

    for item in arr:
        total+=item

    return total


def recursive_sum(arr):
    """
    A function to find the sum of an array using recursion
    :param arr - an array to sum
    :return int
    """

    # base case
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return arr[0]

    return arr[0]+recursive_sum(arr[1:])


## ===== Exercise 4.2
def recursive_count(arr):
    """
    A function to count the nummber of items in an aarray using recursion
    :param arr - an array to count
    :return int - th ecounts of the array
    """

    if not arr:
        return 0

    return 1+recursive_count(arr[1:])

def recursive_max(arr):
    """
    A recursive function to find the maximum number in a list
    :param arr: the lists of elements
    :Return int 
    """

    if len(arr)==1:
        return arr[0]

    sub_max=recursive_max(arr[1:])

    if arr[0]>sub_max:
        return arr[0]
    else:
        return sub_max

def recursive_max_v2(arr,index):
    # base case - checking till the last index
    if index==(len(arr)-1):
        return arr[index]

    # check other the next item in the arru
    sub_max=recursive_max_v2(arr,index+1)



    return arr[index] if arr[index]>sub_max else sub_max


def recursive_binary_search(arr, target, low, high):
    """
    A function to recursively run a binary search algo
    """

    #base case 1: if target is not found:
    if low<high:
        return None
    
    mid=(low+high)//2
    guess=arr[mid]

    # base case 2: if the target is found
    if guess==target:
        return mid

    if guess>target:
        return recursive_binary_search(arr,target,low, mid-1 )
    else:
        return recursive_binary_search(arr, target, mid+1, high)

def multiplication_table(arr):
    """
    Provided an array of numbers we create the multiplicaain table for each of teh eelememts

    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(f"{arr[i]*arr[j]} ", end="")
        print("\n")


arr_1=[1,2,3,5,4,6,8]
print(sum(arr_1))
print(recursive_count(arr_1))
print(recursive_max(arr_1))
print(recursive_max_v2(arr_1,0))
multiplication_table([1,2,3])
