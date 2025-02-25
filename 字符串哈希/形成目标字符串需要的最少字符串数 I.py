from random import randint
from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        # 多项式字符串哈希（方便计算子串哈希值）
        MOD = 1_070_777_777
        BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base = [1] + [0] * n  # 这个是保存BASE的1...n次方，后面避免重复计算
        pre_hash = [0] * (n + 1)  # 字符串前缀哈希值
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD  # pow_base[2] 代表base^2
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶算法计算多项式哈希
            # pre_hash[1] 代表 s0的hash值 pre_hash[i]代表s0....si-1的hash值

        # 计算子串 target[l:r] 的哈希值
        def sub_hash(l: int, r: int) -> int:
            if l == r:  # 如果l等于r则代表target[l:l]的hash值，直接返回ASCII码即可
                return ord(target[l])
            else:
                return (pre_hash[r + 1] - pre_hash[l] * pow_base[r - l+1]) % MOD

        # 将每个words[i]的子串按长度存放到集合sets中，方便后面对比指定长度的字符串是否可以被匹配
        max_len = max(map(len, words))
        sets = [set() for _ in range(max_len)]
        # sets[0]代表长度为1的words[i]子串hash值集合  注意下标从0开始

        # 计算words中所有word的全部子串hash值
        for w in words:
            h = 0
            for j, b in enumerate(w):
                h = (h * BASE + ord(b)) % MOD
                sets[j].add(h)

        '''
        下面的代码思路就是跳跃游戏II的双指针解法
        可以参考我的文章：https://blog.csdn.net/m0_52238102/article/details/144597941
        '''
        ans = 0
        border = 0  # 上一步能到的最右端点
        current_right = 0  # 寻找下一步能够到的最右端点
        for i in range(n):
            while current_right < n and current_right - i < max_len and sub_hash(i, current_right) in sets[current_right - i]:
                current_right += 1  # 找到能走的最右端点
            if i == border:  # 到达当前步数的最右端点
                if i == current_right:  # 当前无法再往后走了
                    return -1
                border = current_right  # 保存下一步能到的最右端点
                ans += 1  # 开始下一步
        return ans


solu = Solution()
print(solu.minValidStrings(["abcdef"], "xyz"))
