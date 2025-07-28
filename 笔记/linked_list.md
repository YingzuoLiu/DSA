# 🔗 Linked List 题型总结（LeetCode）

链表是数据结构中常考的经典类型，以下列出了常见题型和背后的通用模板技巧，便于以后举一反三。

---

---

## 📌 模板总结

### 🔁 链表反转（Reverse Linked List）

```python
def reverseList(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
```

---

### 🔁 快慢指针找环（Linked List Cycle）

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

### 🧮 倒数第 N 个节点删除（Remove Nth from End）

```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next
```

---

### 🔀 重排链表（Reorder List）

```python
def reorderList(head):
    if not head or not head.next: return
    # 1. 找中点
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 2. 反转后半段
    second = reverseList(slow.next)
    slow.next = None
    # 3. 合并两段
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next, second.next = second, tmp1
        first, second = tmp1, tmp2
```

---

### 🧵 合并两个有序链表（Merge Two Sorted Lists）

```python
def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

---

### 🧮 合并 K 个有序链表（Merge K Sorted Lists）

```python
import heapq
def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode()
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

---

## 🧠 统一技巧总结

- **虚拟头节点 dummy**：统一边界情况处理
- **快慢指针**：找中点、判断有无环、倒数第 N 项
- **链表反转**：经典三指针，常用于重排/回文等
- **小顶堆**：合并多个链表时保持顺序（题 23）
- **画图理解指针移动顺序！**

---

