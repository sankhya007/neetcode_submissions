class Solution(): 
    def reverseString(self, s): 
        left = 0 
        right = len(s) - 1
        #here we are using the two pointer function 

        while left < right: 
            s[left] ,s[right] = s[right], s[left]
            left += 1
            right -= 1 

        return None

string = list("neet")

solution = Solution()
solution.reverseString(string)
# really??? we really just had to use 'reverseStrng' and nothing else works? are we really this petty bro ?

print(string)





