class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanum(char):
            return ((ord('a') <= ord(char) <= ord('z')) or 
                    (ord('A') <= ord(char) <= ord('Z')) or
                    ord('0') <= ord(char) <= ord('9'))

        l = 0
        r = len(s) - 1

        while l <= r:
            while not isalphanum(s[l]) and l < r:
                l += 1
            while not isalphanum(s[r]) and r > l:
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1

            else:
                return False

        return True