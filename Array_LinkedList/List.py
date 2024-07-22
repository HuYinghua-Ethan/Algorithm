""""
列表是一个抽象的数据结构概念，它表示元素的有序集合，支持元素访问、修改、添加、删除和遍历等操作
无须使用者考虑容量限制的问题

当使用数组实现列表时，长度不可变的性质会导致列表的实用性降低。
我们可以使用动态数组(dynamic array)来实现列表。它继承了数组的各项优点，并且可以在程序运行过程中进行动态扩容。
"""


# 简易版列表
class MyList:
    """列表类"""

    def __init__(self):
        """构造方法"""
        self._capacity: int = 10
        self._arr: list[int] = [0] * self._capacity
        self._size: int = 0
        self._extend_ratio: int = 2

    def size(self):
        """获取列表长度（当前元素数量）"""
        return self._size

    def capacity(self):
        """获取列表容量"""
        return self._capacity

    def get(self, index):
        """访问元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]

    def set(self, num, index):
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def add(self, num):
        """在尾部添加元素"""
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num, index):
        """在中间插入元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
            self.extend_capacity()
        # 将索引 index 以及之后的元素都向后移动一位
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        self._size += 1

    def remove(self, index):
        """删除元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        # 索引 i 之后的元素都向前移动一位
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        self._size -= 1
        return num

    def extend_capacity(self):
        """列表扩容"""
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        self._capacity = len(self._arr)
    def to_array(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[: self._size]


"""Driver Code"""
if __name__ == "__main__":
    # 初始化列表
    nums = MyList()
    # 在尾部添加元素
    nums.add(1)
    nums.add(3)
    nums.add(2)
    nums.add(5)
    nums.add(4)

    # 在中间插入元素
    nums.insert(6, index=3)

    # 删除元素
    nums.remove(3)

    # 访问元素
    num = nums.get(1)

    # 更新元素
    nums.set(0, 1)

    # 测试扩容机制
    for i in range(10):
        nums.add(i)







