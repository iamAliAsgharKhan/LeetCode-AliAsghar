class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #make a copy of nums    
        tempnums = nums.copy()
        #remove all instances of val from tempnums
        while val in tempnums:
            tempnums.remove(val)
        #replace part of nums with tempnums
        nums[:len(tempnums)] = tempnums
        
        return len(tempnums)