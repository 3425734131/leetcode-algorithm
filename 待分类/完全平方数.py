import bisect

class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        dp = [0]*(n+1)
        for i in range(1,n+1):
            temp = i*i
            if temp > n:
                break
            dp[temp] = 1
            arr.append(temp)
        for i in range(1,n+1):
            if dp[i] == 0:
                temp = i
                result = 0
                while temp != 0:
                    index = bisect.bisect_right(arr, temp) - 1
                    temp = temp - arr[index]
                    result += dp[arr[index]]
                dp[i] = result
        for i,v in enumerate(dp):
            print(f'i={i}, v={v}')

solution = Solution()
solution.numSquares(12)