from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] * (len(s)+1)
        return self.match(s, wordDict,dp)

    def match(self, subString: str, wordDict: List[str],dp:List[bool]) -> bool:
        if not dp[len(subString)]:
            return False
        if subString is None or len(subString) == 0:
            return True
        for word in wordDict:
            if subString.startswith(word) and self.match(subString[len(word):], wordDict,dp):
                return True
        dp[len(subString)] = False
        return False


solution = Solution()
print(solution.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                         ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
