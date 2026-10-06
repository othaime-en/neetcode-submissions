class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())
        return cleaned.lower() == cleaned[::-1].lower()