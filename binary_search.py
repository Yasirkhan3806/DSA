arr = [2,6,5,3,5]
arr.sort()
target = 4
right = len(arr) - 1
left = 0
print(arr)

while left <= right:
    mid = int((left + right) / 2)
    if arr[mid] == target:
        print(mid)
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
