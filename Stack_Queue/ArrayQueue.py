class ArrayQueue:
    """基于环形数组实现的队列"""
    def __init__(self, size):
        self._nums: list[int] = [0] * size  # 用于存储队列元素的数组
        self._front: int = 0  # 队首指针，指向队首元素
        self._size: int = 0  # 队列长度

    def capacity(self):
        """获取队列的容量"""
        return len(self._nums)
    
    def size(self) -> int:
        """获取队列的长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return self._size == 0
    
    def push(self, num):
        if self._size == self.capacity():
            raise IndexError("队列已满")
        # 计算队尾指针，指向队尾索引 + 1
        # 通过取余操作实现 rear 越过数组尾部后回到头部
        rear = (self._front + self._size) % self.capacity()
        self._nums[rear] = num
        self._size += 1

    def pop(self):
        num = self.peek()
        # 队首指针向后移动一位，若越过尾部，则返回到数组头部
        self._front =  (self._front + 1) % self.capacity()
        self._size -= 1
        return num
    
    def peek(self):
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._nums[self._front]
    
    def to_list(self):
        res = [0] * self.size()
        j = self._front
        for i in range(self.size()):
            res[j] = self.nums[j % self.capacity()]
            j += 1
        return res
    
        
if __name__ == "__main__":
    # 初始化队列
    queue = ArrayQueue(10)

    # 元素入队
    queue.push(1)
    queue.push(3)
    queue.push(2)
    queue.push(5)
    queue.push(4)

    # 访问队首元素
    peek = queue.peek()
    print("队首元素 peek =", peek)

    # 元素出队
    pop = queue.pop()
    print("出队元素 pop =", pop)

    # 获取队列的长度
    size = queue.size()
    print("队列长度 size =", size)

    # 判断队列是否为空
    is_empty = queue.is_empty()
    print("队列是否为空 =", is_empty)



