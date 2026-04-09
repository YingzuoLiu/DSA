import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []   # 最小堆，存放 (节点值, 链表编号, 节点对象)

        # 先把每个链表的头节点放进堆里
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)   # 虚拟头节点
        curr = dummy          # 当前结果链表尾部

        # 只要堆不空，就不断取出最小节点
        while heap:
            val, i, node = heapq.heappop(heap)   # 弹出最小节点
            curr.next = node                     # 接到结果链表后面
            curr = curr.next                     # 尾指针后移

            # 如果这个节点后面还有节点，就把下一个节点放进堆
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next   # 返回真正头节点
