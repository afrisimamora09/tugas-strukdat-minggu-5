import random

def insertionSort(arr):
    a = arr.copy()
    comp = 0
    swap = 0

    for i in range(1,len(a)):
        key = a[i]
        j = i-1

        while j >=0 and a[j] > key:
            comp += 1
            a[j+1] = a[j]
            j -= 1
            swap += 1

        a[j+1] = key

    return a, comp, swap


def selectionSort(arr):
    a = arr.copy()
    comp = 0
    swap = 0

    for i in range(len(a)):
        min_idx = i
        for j in range(i+1,len(a)):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1

    return a, comp, swap


def hybridSort(seq, threshold=10):
    if len(seq) <= threshold:
        return insertionSort(seq)
    else:
        return selectionSort(seq)


sizes = [50,100,500]

print("Size | Hybrid Ops | Insertion Ops | Selection Ops")

for s in sizes:

    arr = [random.randint(1,1000) for _ in range(s)]

    _, c1, s1 = hybridSort(arr)
    _, c2, s2 = insertionSort(arr)
    _, c3, s3 = selectionSort(arr)

    print(s,"|",c1+s1,"|",c2+s2,"|",c3+s3)