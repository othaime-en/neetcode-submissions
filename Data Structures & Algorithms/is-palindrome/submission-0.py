class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum())
        print(string)
        return string.lower() == string[::-1].lower()