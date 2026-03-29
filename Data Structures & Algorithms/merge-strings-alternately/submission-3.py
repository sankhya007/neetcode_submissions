class Solution:
    def mergeAlternately(self, word1, word2):
        i = 0
        j = 0
        # here we are starting from the index 0 
        result = []

        while i < len(word1) and j < len(word2): 
                result.append(word1[i])
                # they are seperately appending their letters in the result array
                result.append(word2[j])
                i += 1
                j += 1
                # additon by one 

        result.append(word1[i::])
        # start:end:step format 
        # start is defined by us, end is just the default ending, step is just 1 (default)
        # *** we need to have these appends the 2nd time because it one word could be the length of 3 and the other could be in the length of 7 so when the 1st world which has the length of 3 ends the loop is goiig to end because we have used the and function and thats why the word which have the 7 will have 4 letters left over and that is the reason why wee need to use the append the 2nd time so if there is any left wover lettern we can add them at the end of the merged string***
        result.append(word2[j::])

        return"".join(result)
        # if we would have written return result we would have gotten the output like ['b','r','i'...]
        # by saying "".join(['b','r','i'...]) we get the output like "bri....""

sol = Solution()

string1 = "bristi"
string2 = "sankhya"

print(sol.mergeAlternately(string1, string2))
        