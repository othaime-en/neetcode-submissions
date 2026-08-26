class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for letter in string:
                count[ord(letter) - ord('a')] += 1

            results[tuple(count)].append(string)

        return list(results.values())
