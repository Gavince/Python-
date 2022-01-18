# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 上午8:28
# @Author  : gavin
# @FileName: 98.环形链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
给定一个链表，判断链表中是否有环。

    如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在
环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位
置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作
为参数进行传递，仅仅是为了标识链表的实际情况。如果链表中存在环，则返回 true
。 否则，返回 false 。
进阶：
你能用 O(1)（即，常量）内存解决此问题吗？

解题方法：
(1)哈希表
时间复杂度：O(n)　
空间复杂度：O(n)
(2)快慢指针
时间复杂度：O(n)　
空间复杂度：O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle1(self, head):

        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False

    def hasCycle2(self, head: ListNode) -> bool:

        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False