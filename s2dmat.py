matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16

# for i in range(len(matrix)):
#     first = 0
#     second = len(matrix[i]) - 1
    
#     while first <= second:
#         mid = (first + second) // 2  # Calculate the middle index

#         if matrix[i][mid] == target:
#             print("True")
#             break  # Exit the loop once the target is found
#         elif matrix[i][mid] < target:
#             first = mid + 1  # Move the `first` pointer up
#         else:
#             second = mid - 1  # Move the `second` pointer down

class Solution:
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            first = 0
            second = len(matrix[i]) - 1
    
            while first <= second:
                mid = (first + second) // 2  # Calculate the middle index

                if matrix[i][mid] == target:
                    return True
                    break  # Exit the loop once the target is found
                elif matrix[i][mid] < target:
                    first = mid + 1  # Move the `first` pointer up
                else:
                    second = mid - 1  # Move the `s 
        return False
       
print(Solution().searchMatrix(matrix,target))
