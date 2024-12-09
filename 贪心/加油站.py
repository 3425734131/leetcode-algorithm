from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        column = len(gas)
        remainder = [0] * column
        for i in range(column):
            remainder[i] = gas[i] - cost[i]
        if sum(remainder) < 0:
            return -1
        max_value = 0
        result = 0
        index = 0
        max_index = 0
        flag = True
        for i in range(2*column):
            if flag:
                index = i%column
                flag = False
            result += remainder[i%column]
            if result < 0:
                result = 0
                # 再次开始记录下标
                flag = True
            if result > max_value:
                max_value = result
                max_index = index
        return max_index
