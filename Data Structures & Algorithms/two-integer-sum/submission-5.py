class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myList = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in myList:
                return [myList[diff],index]
            myList[value] = index
            
        