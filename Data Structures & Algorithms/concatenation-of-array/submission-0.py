class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array=[]
        n=len(nums)
        for i in range(0, n):
            new_array.append(nums[i])
        for i in range(0, n):
            new_array.append(nums[i])
        return new_array


        