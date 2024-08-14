# arr = [
#     [2,3,5,7],
#     [3,4,6,3],
#     [5,6,8,9],
#     [7,8,9,10]
# ]
# def checking(row_num = 0,col_num = 0) :
#     max_num = arr[row_num][col_num]
#     if col_num == len(arr[row_num]):
#         checking(row_num + 1,0)
#     else:
#         if max_num < arr[row_num][col_num +1]:
#             max_num = arr[row_num][col_num +1]
        
#     checking(row_num, col_num+1)
#     print(max_num, end=" ")

# checking()


    
arr = [
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1]
]

def checking(row_num=0, col_num=0):
    # Base case: If we've reached the end of the rows, return the max_num found
    if row_num == len(arr):
        return 
    
    # Initialize max_num with the first element only on the first call
    if arr[row_num][col_num + 1] == 1:
            
    
    # Update max_num if the current element is greater
    if arr[row_num][col_num] > max_num:
        max_num = arr[row_num][col_num]

    # Move to the next column
    col_num += 1

    # If we've reached the end of the columns in the current row, move to the next row
    if col_num == len(arr[row_num]):
        return checking(row_num + 1, 0, max_num)
    
    # Continue in the current row
    return checking(row_num, col_num, max_num)

# Call the function and print the maximum value
max_value = checking()
print("Maximum value in the array is:", max_value)

