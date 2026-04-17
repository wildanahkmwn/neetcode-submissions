class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #         pass
        enum = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in enum:
                return [enum[diff], i]
            enum[n] = i
        
        