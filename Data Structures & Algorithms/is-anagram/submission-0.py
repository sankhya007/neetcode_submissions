# class Solution:
#     def isAnagram(self, s, t): 
#         s = list(s)
#         t = list(t)

#         left = 0 
#         right = len(s) - 1

#         while left < right: 
#             s[left], s[right] = s[right], s[left]

#             left += 1
#             right -= 1

#         return s == t  
    
                
# sol = Solution()
# statement = "hello"
# check_statement = "olleh"
# print(sol.isAnagram(statement, check_statement))

class Solution: 
    def isAnagram(self, s, t): 
        return sorted(s) == sorted(t)

sol = Solution()
s = "racecar"
t = "carrace"
print(sol.isAnagram(s, t))

