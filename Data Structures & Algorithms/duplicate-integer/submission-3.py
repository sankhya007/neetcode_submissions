# class Solution:
#     def hasDuplicate(self, arr): 
#         seen = set()
#         duplicate = set()
            # this function is not needed and this is just bringing the time complexity of the code up lol.
            # fuck it we remove whatever we do not need 

#         for i in arr: 
#             if i in seen: 
#                 duplicate.add(i)
#             else: 
#                 seen.add(i)

#         return True if duplicate else False
        
# array = [1,2,3,4,5,6,6,7,8,9]

# solution = Solution()
# print(solution.hasDuplicate(array))


class Solution:
    def hasDuplicate(self, arr): 
        seen = set()

        for i in arr: 
            if i in seen: 
                return True
            seen.add(i)

        return False
        
array = [1,2,3,4,5,6,6,7,8,9]

solution = Solution()
print(solution.hasDuplicate(array))