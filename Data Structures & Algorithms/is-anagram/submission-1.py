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


#this will work but inly for the words those are completely swapped in ther opposite side and will not work if the words are swapped in the string 
# like this will work for the word "hello" and "olleh" but it will not work for the word "hello" and "oellh" because in the 2nd case the letters are not completely swapped in the opposite side and they are just swapped in the string so this is not a good solution for the anagram problem because anagrams can be formed by just swapping the letters in the string and not necessarily by swapping them in the opposite side.
# but the modifies function underneath is going to work for any kinf of cases that you throw at it 

class Solution: 
    def isAnagram(self, s, t): 
        return sorted(s) == sorted(t)

sol = Solution()
s = "racecar"
t = "carrace"
print(sol.isAnagram(s, t))

