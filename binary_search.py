# arr = [2,6,5,3,5]
# arr.sort()
# target = 4
# right = len(arr) - 1
# left = 0
# print(arr)

# while left <= right:
#     mid = int((left + right) / 2)
#     if arr[mid] == target:
#         print(mid)
#     if arr[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# target= int((0+1)/2 )
# print(target)
arr = [3,5,6,8,11,12,14,15,17,18]
target = 16
left = 0
midarr = []
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    print(left,right)
    midarr.append(arr[mid])
    if arr[mid] == target:
        print(mid)
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(midarr)