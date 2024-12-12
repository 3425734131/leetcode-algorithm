from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 第一步 找到中心节点 ------快慢指针
# 第二部 反转后半段列表
# 第三部 判断是否为回文串
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        right = head
        while right.next is not None:
            left = left.next
            right = right.next
            # 快指针走两步
            if right.next is None:
                break
            right = right.next
        # 到这一步left就是中间节点或中间两个节点中的第二个
        # 开始反转链表
        right = left.next
        left.next = None
        while right is not None:
            temp = right.next
            right.next = left
            left = right
            right = temp
        # 当前left就是后半段的头指针
        # 开始判断是否是回文链表
        while left is not None:
            if head.val != left.val:
                return False
            head = head.next
            left = left.next
        else:
            return True


soultion = Solution()
head = ListNode(val=0)
current = ListNode(val=1)
head.next = current
print(soultion.isPalindrome(head))


