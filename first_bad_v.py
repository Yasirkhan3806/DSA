def isbadVersion(version,arr):
    arr.sort()
    first = 0
    second = len(arr) - 1

    while first <= second:
        mid = (first + second) // 2
        if arr[mid] == version:
            return arr[mid:-1]
        elif arr[mid] > version:
            second = mid - 1
        else:
            first = mid + 1
    return False

arr = [3,5,7,4,4,7,7,3,2]
version = 5
print(isbadVersion(version,arr))
        