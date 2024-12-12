from typing import List

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         column = len(gas)
#         remainder = [0] * column
#         for i in range(column):
#             remainder[i] = gas[i] - cost[i]
#         if sum(remainder) < 0:
#             return -1
#         max_value = 0
#         result = 0
#         index = 0
#         max_index = 0
#         flag = True
#         for i in range(2*column):
#             if flag:
#                 index = i%column
#                 flag = False
#             result += remainder[i%column]
#             if result < 0:
#                 result = 0
#                 # 再次开始记录下标
#                 flag = True
#             if result > max_value:
#                 max_value = result
#                 max_index = index
#         return max_index

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        column = len(gas)
        remainder = [0] * column
        for i in range(column):
            remainder[i] = gas[i] - cost[i]
        if sum(remainder) < 0:
            return -1
        # 如果总和不为负数，那么一定可以找到从一个点开始，能遍历全部
        qianzhui = 0
        index = 0

        while index < column:
            for j in range(index, column):
                qianzhui += remainder[j]
                if qianzhui < 0:  # 汽油不够了
                    qianzhui = 0
                    index = j+1
                    break
            else:
                return index


solution = Solution()
print(solution.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]))


