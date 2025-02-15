#MERGE SORT explained
arr_test = [2,3,5,1,7,4,4,4,2,6,0]

def merge_sort(arr):
  if len(arr) > 1:
    left_arr = arr[0:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    #recursion
    merge_sort(left_arr)
    merge_sort(right_arr)

    # merge
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] < right_arr[j]:
        arr[k] = left_arr[i]
        i += 1
      else:
        arr[k] = right_arr[j]
        j += 1
      k += 1

    # remaining elements from left_arr
    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1

    # remaining elements from right_arr
    while j < len(right_arr):
      arr[k] = right_arr[j]
      j += 1
      k += 1

print("Original array:", arr_test)

merge_sort(arr_test)

print("Sorted array:", arr_test)