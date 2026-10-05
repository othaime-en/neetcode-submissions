class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = defaultdict(int)

        # create a frequency map where the keys are the nums
        # and the values is the frequency the number appears
        for num in nums:
            result[num] += 1
        
        output = []
        for _ in range(k):
            maxnum = max(result, key=result.get)
            output.append(maxnum)
            result.pop(maxnum)

        return output