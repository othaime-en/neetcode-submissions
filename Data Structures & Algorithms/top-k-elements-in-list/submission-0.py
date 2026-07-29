class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        output=[]

        nums.sort()
        for num in nums:
            result[num] = 1 + result.get(num,0)

        dict = result
        for n in range(k):
            most_freq=max(dict, key=result.get)
            output.append(most_freq)
            del dict[most_freq]
        
        return output
        