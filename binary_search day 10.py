#Binary search is a fast search algorithm with run-time complexity of Ο(log n).
#This search algorithm works on the principle of divide and conquer.
#For this algorithm to work properly, the data collection should be in the sorted form.
#Binary search looks for a particular item by comparing the middle most item of the collection.
#If a match occurs, then the index of item is returned.
#If the middle item is greater than the item, then the item is searched in the sub-array to the left of the middle item.
#Otherwise, the item is searched for in the sub-array to the right of the middle item.
#This process continues on the sub-array as well until the size of the subarray reduces to zero.



n=int(input("Enter the length of array: "))
print("Enter values in array : ")
a=[int(input()) for i in range(n)]
print("Array: ",a)
key=int(input("Enter the element to be search:" ))
found=0;low=0;high=n-1
while low<=high:
    mid=(low+high)//2
    if key<a[mid]:
        high=mid-1
    elif key>a[mid]:
        low=mid+1
    elif key==a[mid]:
        print("Element found at location:", mid)
        found = 1
        break
if not found:
    print("Element not found")

#Time complexity : O(log2n)
#space complexity : O(1)
