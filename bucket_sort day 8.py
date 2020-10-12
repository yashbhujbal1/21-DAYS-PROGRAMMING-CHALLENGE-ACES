#Bucket sort is also known as bin sort.
#It works by distributing the element into the array also called buckets.
#Buckets are sorted individually by using different sorting algorithm.
#Bucket sort is mainly useful when input is uniformly distributed over a range.
#
#bucketSort(arr[], n)
#1) Create n empty buckets (Or lists).
#2) Do following for every array element arr[i].
#.......a) Insert arr[i] into bucket[n*array[i]]
#3) Sort individual buckets using insertion sort.
#4) Concatenate all sorted buckets.

# Python3 program to sort an array
# using bucket sort

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

        # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

        # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

        # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


# Driver Code
x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))

#Time complexity : θ(n+k)
#space complexity : O(1)