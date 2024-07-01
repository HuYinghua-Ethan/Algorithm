class ArrayStack:
    def __init__(self):
        """构造方法"""
        self._stack = []
        
    def size(self):
        """获取栈的长度"""
        return len(self._stack)
    
    def is_empty(self):
        """"判断栈是否为空"""
        return self._stack == []
    
    def push(self, item):
        """入栈"""
        self._stack.append(item)

    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack.pop()
    
    def peek(self):
        """"访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]
    
    def to_list(self):
        return self._stack

if __name__ == "__main__":
    # 初始化栈
    stack = ArrayStack()

    # 元素入栈
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(3)
    stack.push(3)
    print("栈 stack = ", stack.to_list())

    # 访问栈顶元素
    peek = stack.peek()
    print("栈定元素 peek = ", peek)

    # 元素出栈
    pop = stack.pop()
    print("出栈元素 pop =", pop)
    print("出栈后 stack = ", stack.to_list())

    # 获取栈的长度
    size = stack.size()
    print("栈的长度 size = ", size)

    # 判断栈是否为空
    is_empty = stack.is_empty()
    print("栈是否为空 =", is_empty)
    









