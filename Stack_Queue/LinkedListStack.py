class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListStack:
    def __init__(self):
        """"构造方法"""
        self._peek = None
        self._size = 0
        
    def size(self):
        """获取栈的长度"""
        return self._size
    
    def is_empty(self):
        """判断栈是否为空"""
        return self._size == 0
    
    def push(self, val):
        """入栈"""
        node = ListNode(val)
        node.next = self._peek  # 下一个节点指向栈顶元素
        self._peek = node   # 记录当前节点
        self._size += 1
        
    def pop(self):
        """"出栈"""
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self):
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val
    
    def to_list(self):
        """转化为列表用于打印"""
        arr =  []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr


if __name__ == "__main__":
    # 初始化栈
    stack = LinkedListStack()
    
    # 元素入栈
    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print("栈 stack = ", stack.to_list())

    # 访问栈顶元素
    peek = stack.peek()
    print("栈顶元素: ", peek)

    # 元素出栈
    pop = stack.pop()
    print("出栈元素: ", pop)
    print("出栈后栈 stack = ", stack.to_list())

    # 获取栈的长度
    size = stack.size()
    print("栈的长度: ", size)

    # 判断栈是否为空
    is_empty = stack.is_empty()
    print("栈是否为空 : ", is_empty)

    

