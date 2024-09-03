# def smallest(letters,target):
#     first = 0
#     second = len(letters) - 1
#     while first <= second:
#         mid = (first + second) // 2
#         if letters[mid] > target:
#             second = mid
#             m = (first + second) // 2
#             if letters[m] > target:
#                 return letters[m]
#             elif target > letters[m]:
#                 first = m + 1
#             else:
#                 return letters[mid]
            
#         elif letters[mid] < target:
#             first = mid + 1
#         else:
#             second = mid - 1

#     return letters[0]

# # # letters = [1,3,5,7]
# # # target = -2
# letters = ["x","x","y","y"]
# target ="z"
# print(smallest(letters,target))

# # # def smallest(letters, target):
# # #     first = 0
# # #     last = len(letters) - 1
    
# # #     while first <= last:
# # #         mid = (first + last) // 2
# # #         if letters[mid] < target:
# # #             first = mid + 1
# # #         else:
# # #             last = mid - 1
    
# # #     # After the loop, `first` is the smallest index where `letters[first] >= target`
# # #     if first < len(letters) and letters[first] >= target:
# # #         return letters[first]
# # #     return []

# # # # Example usage
# # # letters = [1, 3, 5, 25]
# # # target = 23
# # # print(smallest(letters, target))  # Output: 1

# # # print('a'> 'c')
# # letters = ["c","f","j"]
# # print(letters[0] > letters[1])
# # def nextGreatestLetter(letters, target):
# #         """
# #         :type letters: List[str]
# #         :type target: str
# #         :rtype: str
# #         """
# #         first = 0
# #         second = len(letters) - 1
# #         while first < second:
# #             mid = (first + second) // 2
# #             if target > letters[mid]:
# #                 first = mid + 1
# #             else:
# #                 second = mid - 1
            
# #             if first < len(letters) and letters[first] > target:
# #                 return letters[first]
# #             elif first < len(letters) and letters[first] == target:
# #                 return letters[first + 1]
# #             elif first < len(letters) and letters[first] < target:
# #                 return letters[first + 1]
# #             else: 
# #                  return letters[0]
        
            
# # letters =["c","f","j"]
# # target ="d"
            
# # print(nextGreatestLetter(letters,target))

# print((0 + 0) // 2)