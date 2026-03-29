class Solution:
    def validPalindrome(self, s): 
        def isPalindrome(l, r): 
            while l < r: 
                if s[l] != s[r]: 
                    return False
                else: 
                    l += 1
                    r -= 1
            return True
        left = 0 
        right = len(s) - 1

        while left < right: 
            if s[left] != s[right]: 
                # here we just have to perform left skip or right skip
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
                # by doing the left +1 we are just moving the left index 1 point towards the right side 
                # by doing the right -1 we ar ejust moving the right index 1 point towards the left side
            else: 
                left += 1
                right -= 1
        return True 

sol = Solution()

statement = "abba"
print(sol.validPalindrome(statement))
        