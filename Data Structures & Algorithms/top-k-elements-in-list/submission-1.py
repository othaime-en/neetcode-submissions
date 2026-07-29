class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        output=[]

        nums.sort()
        for num in nums:
            result[num] = 1 + result.get(num,0)

        for n in range(k):
            most_freq=max(result, key=result.get)
            output.append(most_freq)
            del result[most_freq]
        
        return output
        