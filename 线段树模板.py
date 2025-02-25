class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 线段树数组，大小为 4n
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """构建线段树"""
        if start == end:
            # 这次构建的叶子节点，直接存储数组中的值
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1  # 左子节点
            right_node = 2 * node + 2  # 右子节点
            # 递归构建左右子树
            self.build(arr, left_node, start, mid)
            self.build(arr, right_node, mid + 1, end)
            # 当前节点的值为左右子树的最大值
            self.tree[node] = max(self.tree[left_node], self.tree[right_node])

    def query(self, node, start, end, L, R):
        """查询区间 [L, R] 的最大值
            :param node: 查询的节点
            :param start: 每次要遍历的范围
            :param end: 每次要遍历的范围
            :param L: 最终查询的左边界
            :param R: 最终查询的右边界
            :return: 返回查询区间的最大值
        """
        if R < start or L > end:
            # 当前节点区间与查询区间无交集
            return -float('inf')
        if L <= start and end <= R:
            # 当前节点区间完全包含在查询区间内
            return self.tree[node]
        mid = (start + end) // 2
        left_max = self.query(2 * node + 1, start, mid, L, R)  # 查询左子树
        right_max = self.query(2 * node + 2, mid + 1, end, L, R)  # 查询右子树
        return max(left_max, right_max)  # 返回左右子树的最大值

    def update(self, node, start, end, idx, value):
        """更新数组中的某个元素"""
        if start == end:
            # 找到叶子节点，更新值
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if idx <= mid:
                # 需要更新的位置在左子树
                self.update(left_node, start, mid, idx, value)
            else:
                # 需要更新的位置在右子树
                self.update(right_node, mid + 1, end, idx, value)
            # 更新当前节点的值为左右子树的最大值
            self.tree[node] = max(self.tree[left_node], self.tree[right_node])

# 使用示例
arr = [1, 3, 2, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(0, 0, len(arr) - 1, 1, 4))  # 查询区间 [1, 4] 的最大值，输出 9
st.update(0, 0, len(arr) - 1, 2, 10)  # 将下标 2 的值更新为 10
print(st.query(0, 0, len(arr) - 1, 1, 4))  # 再次查询区间 [1, 4] 的最大值，输出 10