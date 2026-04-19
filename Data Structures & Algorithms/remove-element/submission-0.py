class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        write_index=0
        for i in range(0,n):
            if nums[i]!=val:
                nums[write_index]=nums[i]
                write_index+=1
        return(write_index)
                