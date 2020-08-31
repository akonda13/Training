def insertion_sort(arr):
    indexing_length = range(1, len(arr))
    for key in indexing_length:
        while arr[key-1] > arr[key] and key>0:
            arr[key], arr[key-1] = arr[key-1], arr[key]
            key = key - 1
            print (arr)

l = [6, 8,1, 4, 10]
print(l)
print (insertion_sort(l))


# O(n2)
