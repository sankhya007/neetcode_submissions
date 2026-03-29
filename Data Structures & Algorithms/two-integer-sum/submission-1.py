class Solution(): 
    def twoSum(self, arr, target): 
        seen = {}  #here we are actually saving the index of the values taht we have in the array

        for i in range(len(arr)):  
            num = arr[i]   # we are extracting the number through the indexes 
            complement = target - num     # checking for the complement(see what number we need)

            if complement in seen: # checking if the num comeplement is in the seen 
                return [seen[complement], i]  
                # getting the indexes of the numbers from seen
                # the complement index is estracted from the the seen 
                # i is the number that we alreayd have 

            seen[num] =  i
            # this line is actuallt storing the numbers from the array n the {}
            # it also notes down the indexes and the stores them like this 
            #{1:0, 2:1, 3:2, 4:3..........}

        return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
solution = Solution()
print("the indexes are: ", solution.twoSum(array, target))