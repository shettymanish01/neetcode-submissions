class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.part = []
        self.s = s
        self.partition_palindromes(0)
        return self.res


    def partition_palindromes(self, i):
        if i == len(self.s):
            self.res.append(self.part.copy())
            return

        for j in range(i, len(self.s)):
            if self.is_palindrome(i, j):
                self.part.append(self.s[i:j+1])
                self.partition_palindromes(j+1)
                self.part.pop()
            
    def is_palindrome(self, l, r):
        while l < r:
            if self.s[l] != self.s[r]:
                return False
            l += 1
            r -= 1
        return True
    
