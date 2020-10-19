#Fibonacci search technique is a method of searching a sorted array using a divide and conquer algorithm that narrows down
#possible locations with the aid of Fibonacci numbers.
# Compared to binary search where the sorted array is divided into two equal-sized parts, one of which is examined further,
# Fibonacci search divides the array into two parts that have sizes that are consecutive Fibonacci numbers.
#Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to search an element in a sorted array.



def fibsearch(a,x,n):
    fib2=0
    fib1=1
    fib=fib1+fib2

    while fib<n:
        fib2=fib1
        fib1=fib
        fib=fib1 + fib2
    offset=0

    while fib>1:
        i=min(offset+fib2,n)
        if a[i]<x:
            fib=fib1
            fib1=fib2
            fib2=fib-fib1
            offset=i
        elif a[i]>x:
            fib = fib2
            fib1 = fib1-fib2
            fib2 = fib - fib1
        else:
            return i

    return -1

n=int(input("Enter the length of array: "))
print("Enter values in array : ")
a=[int(input()) for i in range(n)]
print("Array: ",a)
x=int(input("Enter the element to be search:" ))
a=fibsearch(a,x,n)
print("found at loc: ",a)

#Time complexity :  O(log N)
#space complexity : O(n)

