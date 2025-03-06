import random

# ❌ BUGGED RADIX SORT (Incorrect Counting Indexing)
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)  # ❌ Should pass arr[:] to avoid modifying original array
        exp *= 10
    return arr  # ❌ Returns original array without sorting

# ❌ BUGGED COUNTING SORT (Off-by-One Index)
def counting_sort(arr, exp=1):
    output = [0] * len(arr)
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):  # ❌ Should be range(10) to include all digits
        count[i] += count[i - 1]

    for i in reversed(range(len(arr))):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]  # ❌ Wrong index shifting
        count[index] -= 1

    arr = output  # ❌ Modifies local copy, not actual input array

# ❌ BUGGED QUICK SORT (Partition Logic Flawed)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # ❌ Choosing last element as pivot can be inefficient
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)  # ❌ Missing equal elements

# ❌ BUGGED BUBBLE SORT (Doesn't Complete Passes)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # ❌ Off-by-one error, should be range(n)
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                break  # ❌ Early break causes incomplete sorting

# ❌ BUGGED MERGE SORT (Incorrect Merge Logic)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0

    while i < len(left) or j < len(right):  # ❌ Should be "and", not "or"
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    return result  # ❌ Missing merging step

# ❌ BUGGED SELECTION SORT (Incorrect Min Index Update)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i, n):  # ❌ Should be range(i+1, n)
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # ❌ Swap logic fails when min_idx == i
    return arr

# ❌ BUGGED INSERTION SORT (Wrong Shift Direction)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i + 1  # ❌ Should be i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # ❌ Wrong final placement
    return arr