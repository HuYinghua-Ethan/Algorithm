"""
内存空间是所有程序的公共资源，在一个复杂的系统运行环境下，空闲的内存空间可能散落在内存各处
存储数组的内存空间必须是连续的，而数组非常大时，内存可能无法提供如此大的连续空间
此时，链表的灵活性优势就体现出来了


链表是一种线性的数据结构，其中的每个元素都是一个节点对象，各个节点通过“引用”相连接
引用记录了下一个节点的内存地址，通过它可以从当前节点访问到下一个节点

链表的设计使得各个节点可以分散存储在内存各处，它们的内存地址无须连续

链表的组成单位是节点，每个节点都包含两项数据：节点的值和指向下一节点的引用
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 插入节点
"""在相邻两个节点n0和n1之间插入一个新的节点P,则只需改变两个节点引用（指针）即可"""
def insert(n0, P):
    n1 = n0.next
    P.next = n1
    n0.next = P


# 删除节点
"""在链表删除节点，只需改变一个节点的引用（指针）即可"""
def remove(no):
    P = n0.next
    n1 = P.next
    n0.next = n1

# 访问节点
"""在链表中访问节点的效率较低"""
"""程序需要从头节点出发，逐个向后遍历，直至找到目标节点为止"""
"""访问链表的第 i 个节点需要循环 i - 1 轮"""
def access(head, index):
    for _ in range(index):
        if not head:
            return
        head = head.next


# 查找节点
def find(head, target):
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

    
if __name__ == "__main__":
    # 链表初始化
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)

    # 构建节点之间的引用
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    index = find(n0, 2)
    print("链表中值为2的节点索引为: ", index)











