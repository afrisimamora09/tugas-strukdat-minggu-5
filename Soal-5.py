# Brute Force O(n²)
def countInversionsNaive(arr):

    count = 0

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count += 1

    return count

# Merge Sort O(n log n)
def mergeCount(left,right):

    i=j=0
    merged=[]
    inv=0

    while i<len(left) and j<len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            inv += len(left)-i
            j+=1

    merged += left[i:]
    merged += right[j:]

    return merged,inv


def mergeSortCount(arr):

    if len(arr)<=1:
        return arr,0

    mid=len(arr)//2

    left,invL = mergeSortCount(arr[:mid])
    right,invR = mergeSortCount(arr[mid:])

    merged,invM = mergeCount(left,right)

    return merged, invL+invR+invM


def countInversionsSmart(arr):
    _,inv = mergeSortCount(arr)
    return inv

# Contoh
import random
import time

sizes=[1000,5000,10000]

for s in sizes:

    arr=[random.randint(1,10000) for _ in range(s)]

    start=time.time()
    naive=countInversionsNaive(arr)
    t1=time.time()-start

    start=time.time()
    smart=countInversionsSmart(arr)
    t2=time.time()-start

    print("Size:",s)
    print("Naive:",t1)
    print("Merge:",t2)
    print()