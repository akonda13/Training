def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr.pop()

    smaller, larger = [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        else:
            larger.append(num)

    return quick_sort(smaller) + [pivot] + quick_sort(larger)  # perform quicksort on smaller and larger lists
    # return quick_sort(smaller) + [pivot] + quick_sort(larger)

arr = [42, 38, 39, 20, 27, 46, 10, 5, 34, 13]


s=quick_sort(arr)
print (s)
