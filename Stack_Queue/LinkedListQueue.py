""""
基于链表实现队列
可以将链表的“头节点”和“尾节点”分别视为“队首”和“队尾”
规定队尾仅可添加节点，队首仅可删除节点
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListQueue:
    def __init__(self):
        """构造方法"""
        self._front = None
        self._rear = None
        self._size = 0

    def size(self):
        """"获取队列的长度"""
        return self._size
    
    def is_empty(self):
        """"判断队列是否为空"""
        return not self._front
    
    def push(self, num):
        """"入队"""
        # 在为节点后面添加 num
        node = ListNode(num)
        # 如果队列为空，则令头、尾节点都指向该节点
        if self._front is None:
            self._front = node
            self._rear = node
        # 如果队列不为空，则将该节点添加到尾节点后
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def pop(self):
        num = self.peek()
        self._front = self._front.next
        self._size -= 1
        return num
        
    def peek(self):
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val
        
    def to_list(self):
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue

    
if __name__ == "__main__":
    # 初始化队列
    queue = LinkedListQueue()

    # 元素入队
    queue.push(1)
    queue.push(3)
    queue.push(2)
    queue.push(5)
    queue.push(4)
    print("队列 queue =", queue.to_list())

    # 访问队首元素
    peek = queue.peek()
    print("队首元素 front =", peek)

    # 元素出队
    pop_front = queue.pop()
    print("出队元素 pop =", pop_front)
    print("出队后 queue =", queue.to_list())

    # 获取队列的长度
    size = queue.size()
    print("队列长度 size =", size)

    # 判断队列是否为空
    is_empty = queue.is_empty()
    print("队列是否为空 =", is_empty)






