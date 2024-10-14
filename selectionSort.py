def swap(value1, value2):
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2

def selectionSort(array):
    for fillslot in range(len(array)):
        positionOfMin = fillslot
        # Find the index of the smallest value in the remaining unsorted portion
        for location in range(fillslot + 1, len(array)):
            if array[location] < array[positionOfMin]:
                positionOfMin = location
        
        # Swap the current position with the smallest value found
        array[fillslot], array[positionOfMin] = swap(array[fillslot], array[positionOfMin])

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        # Track whether a swap was made
        swapped = False
        # Traverse the array from 0 to n-i-1
        # The last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

# Example usage
array = [64, 25, 12, 22, 11]
bubbleSort(array)
print(array)
