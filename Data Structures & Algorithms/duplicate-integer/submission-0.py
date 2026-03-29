class Solution:
    def hasDuplicate(self, arr): 
        seen = set()
        duplicate = set()

        for i in arr: 
            if i in seen: 
                duplicate.add(i)
            else: 
                seen.add(i)

        return True if duplicate else False
        
array = [1,2,3,4,5,6,6,7,8,9]

solution = Solution()
print(solution.hasDuplicate(array))
