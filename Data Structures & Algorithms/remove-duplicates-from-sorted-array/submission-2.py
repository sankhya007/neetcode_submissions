class Solution:
    def removeDuplicates(self, nums): 
        if not nums: 
            return 0 

        k = 1 # we have this because we are just going to keep the 1st eleemt there becuse the 1st element can never be duplicate 
        for i in range(1, len(nums)): 
            if nums[i] != nums[k - 1]: 
                # we compare 0th index to 1st index if they same we tell them to fuck off 
                # if they not same we add that to the array 
                nums[k] = nums[i]
                k += 1
        
        return k 

sol = Solution()
array = [1, 1, 2, 3, 3, 4, 4, 5]
print(sol.removeDuplicates(array))
