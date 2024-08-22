def smallest(arr,target):
    first = 0
    second = len(arr) - 1
    while first <= second:
        mid = (first + second) // 2
        if arr[mid] > target:
            second = mid
            m = (first + second) // 2
            if arr[m] > target:
                return arr[m]
            elif target > arr[m]:
                first = m + 1
            else:
                return arr[mid]
            
        elif arr[mid] < target:
            first = mid + 1
        elif target == arr[mid]:
            return arr[mid]
        else:
            second = mid - 1

    return []

arr = [1,3,5,7]
target = -2
print(smallest(arr,target))

# def smallest(arr, target):
#     first = 0
#     last = len(arr) - 1
    
#     while first <= last:
#         mid = (first + last) // 2
#         if arr[mid] < target:
#             first = mid + 1
#         else:
#             last = mid - 1
    
#     # After the loop, `first` is the smallest index where `arr[first] >= target`
#     if first < len(arr) and arr[first] >= target:
#         return arr[first]
#     return []

# # Example usage
# arr = [1, 3, 5, 25]
# target = 23
# print(smallest(arr, target))  # Output: 1
