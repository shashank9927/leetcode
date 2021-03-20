class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		flag = False
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j] == target):
                    flag=True
                    return i, j
        if flag==False:
            return []
