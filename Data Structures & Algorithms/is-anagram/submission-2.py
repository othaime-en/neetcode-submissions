class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        array_s = [0] * 26
        array_t = [0] * 26

        for i in range(len(s)):
            array_s[ord(s[i]) - ord('a')] += 1
            array_t[ord(t[i]) - ord('a')] += 1

        return array_s == array_t

        