# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        smallest = i
        for j in range(i+1, length):
            if (arr[j] < arr[smallest]):
                smallest = j
        placehold = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = placehold
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    temp = 0
    # Your code here

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr


"""
    length = len(arr)
    count = 1
    holder = 0
 while count < length:
      for element in arr:
           if element > arr[count]:
                holder = arr[count - 1]
                arr[count - 1] = arr[count]
                arr[count] = holder
            count += 1
            print(arr)
"""

bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
