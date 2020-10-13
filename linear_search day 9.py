#Linear search is a very simple search algorithm.
#In this type of search, a sequential search is made over all items one by one.
#Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the
#end of the data collection.


n=int(input("Enter the length of array: "))
print("Enter values in array : ")
a=[int(input()) for i in range(n)]
print("Array: ",a)
key=int(input("Enter the element to be search:" ))
found=0
for i in range(0,n):
    if a[i]==key:
        print("Element found at location:", i)
        found=1
        break
if not found:
    print("Element not found")

#Time complexity : O(N)
#space complexity : O(n)


