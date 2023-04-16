class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tempset=set(nums)
        tempnums = sorted(list(tempset))
        nums[0:len(tempnums)]=tempnums
        return len(tempnums)