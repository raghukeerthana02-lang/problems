class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        for val in nums:
            map[val]=map.get(val,0)+1
        a=list(map.values())
        max_val=max(a)
        for key, val in map.items():
            if max_val==val:
                return key
        