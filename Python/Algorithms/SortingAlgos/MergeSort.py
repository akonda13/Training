def create_array(size=10, max=50):
    from random import randint
    return ([randint(0,max) for _ in range(size)])

def merge(a,b):
    print ('merge called == ', a,b)
    c = []
    a_idx, b_idx = 0,0
    while a_idx < len(a) and b_idx <len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx+=1
        else:
            c.append(b[b_idx])
            b_idx+=1

    if a_idx == len(a): c.extend(b[b_idx:])  #Append the elements from the bigger list
    else:               c.extend(a[a_idx:])
    print ('in merge == ',c)
    return c

def merge_sort(a):
    if len(a) <=1:
        print ('single element== ', a)
        return a
    mid = int(len(a)/2)
    print(a)
    print (mid)
    print('a[:mid]== ', a[:mid])
    print('a[mid:]== ', a[mid:])
    left,right = merge_sort(a[:mid]), merge_sort(a[mid:])
    # left = merge_sort(a[:mid])
    # right = merge_sort(a[mid:])
    print ('left--', left)
    print ('right--', right)
    return merge(left,right)



# arr1 = create_array()
# print (arr1)

arr = [42, 38, 39, 20, 27, 46, 10, 5, 34, 13]

# arr2 = create_array()
# arr2.sort()
# print (arr2)

# print (merge(arr1, arr2))

s=merge_sort(arr)
print (s)
