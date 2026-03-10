def bubbleSort(arr):
    a = arr.copy()
    n = len(a)

    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1

        for j in range(0, n-i-1):
            comparisons += 1

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
                swapped = True

        print("Pass", passes, ":", a)

        if not swapped:
            break

    return a, comparisons, swaps, passes


print(bubbleSort([5,1,4,2,8]))
print()
print(bubbleSort([1,2,3,4,5]))