class Solution:
    def merge(self, nums1, m, nums2, n):
        # m is the number of elements in num1
        # n is the number of elements in num2 
        i = m - 1 #works as len(nums1)
        j = n - 1
        # and just we have to modify the num1 (as instructed)
        k = m + n - 1 # number of elemens num1 will have after the merging 

        while i >= 0 and j >= 0: 
            if nums1[i] > nums2[j]: # if the last element in the num1 is biger it gets added at the end
                nums1[k] = nums1[i]
                i -= 1
            else:  #nums1[i] < nums2[j]: 
                nums1[k] = nums2[j] # if the last  element in the num2 is bigger it gets added
                j -= 1
            k -= 1

        while j >= 0: #if the num2 had more elements than num1 then we just add them with this func
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
# this is written like this because the question says us to do it this way and also we do not have to create any extra space in the array 
# we just have add and arrange the numbers from the 2nd array 
m = 3
nums2 = [2, 5, 6]
n = 3
print("the merged array is: ", sol.merge(nums1, m, nums2, n))
