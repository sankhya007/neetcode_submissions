class Solution: 
    def removeElement(self, arr, value):
        k = 0 
        #new_arr = []
        
        for i in range(len(arr)): 
            if arr[i] != value: 
                arr[k] = arr[i]
                k += 1
                #new_arr.append(arr[i])
                # commented out to have time optimized answer

        return k        
        #return new_arr
        # if we want then we can get the array back as well but in this specifc qustion they do not want the array back they just want to know however many elements that we have in ther array and that's it
    
sol = Solution()
array = [1, 2, 3, 4, 5, 2, 6]
value_to_remove = 2
print(sol.removeElement(array, value_to_remove))
