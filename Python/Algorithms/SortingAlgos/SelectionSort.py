def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr [num], arr[spot_marker]
        spot_marker +=1
        print(arr)


    # for marker in range(len(arr)-1):
    #     for num in range(marker, len(arr)):
    #         if arr[num] < arr[marker]:
    #             arr[marker], arr[num] = arr [num], arr[marker]
    #             print (arr)


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print (selection_sort(l))

 # O(n2)
