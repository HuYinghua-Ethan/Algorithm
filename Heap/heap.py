"""
堆是一种满足特殊条件的完全二叉树，主要分为两种类型
小顶堆：任意节点的值 <= 其子节点值
大顶堆：任意节点的值 >= 其子节点值

堆作为完全二叉树的一个特例，具有以下特征：
最底层节点靠左填充，其他层的节点都被填满。
我们将二叉树的根节点称为"堆顶"，将底层最靠右的节点称为"堆底"。
对于大顶堆（小顶堆），堆顶元素（根节点）的值是最大（最小）的。


堆通常用于实现队列，大顶堆相当于元素按从大到小的顺序出队的优先队列


1.堆的存储与表示
完全二叉树非常适合用数组来表示。由于堆正是一种完全二叉树，因此我们将采用数组来存储堆。
当使用数组表示二叉树时，元素代表节点值，索引代表节点在二叉树中的位置。节点指针通过索引映射公式来实现。
给定索引 i ，其左子节点的索引为2i+1，右子节点的索引为2i+2，父节点的索引为(i-1)//2（向下取整）。当索引越界时，表示空节点或节点不存在。


2.访问堆顶元素
堆顶元素即为二叉树的根节点，也就是列表的首个元素


3.元素入堆
给定元素val，首先将其添加到堆底。
由于val可能大于堆中的其他元素，堆的成立条件可能已被破坏，因此需要修复从插入节点到根节点的路径上的各个节点，这个操作被称为堆化
从入堆节点开始，从底至顶执行堆化： 
(1)比较插入节点与其父节点的值，如果插入节点更大，则将它们交换。
(2)继续执行(1)操作，从底到顶修复堆中的各个节点，直至越过根节点或遇到无须交换的节点时结束。


4.堆顶元素出堆
堆顶元素是二叉树的根节点，即列表首元素。
如果我们直接从列表中删除首元素，那么二叉树中所有节点的索引都会发生变化，这将使得后续使用堆化进行修复变得非常困难。
为了尽量减少元素索引的变动，我们采用以下操作步骤：
(1)交换堆顶元素与堆底元素（交换根节点和最右节点）
(2)交换完成后，将堆底从列表中删除（注意，由于已经交换，因此实际上删除的是原来的堆顶元素）。
(3)从根节点开始，从顶至底执行堆化。

“从顶至底堆化”的操作方向与“从底至顶堆化”相反
将根节点的值与其两个子节点的值进行比较，将最大的子节点与根节点交换。
然后循环执行此操作，直到越过叶节点或遇到无须交换的节点时结束。


"""

class MaxHeap:
    """大顶堆"""
    def __init__(self, nums):
        # 将列表元素原封不动添加进堆
        self.max_heaap = nums
    
    def left(self, i):
        """获取左子节点的索引"""
        return 2 * i + 1
    
    def right(self, i):
        """获取右子节点的索引"""
        return 2 * i + 2
    
    def parent(self, i):
        """获取父节点的索引"""
        return (i - 1) // 2

    def size(self):
        """获取堆大小"""
        return len(self.max_heap)
    
    def is_empty(self):
        """判断堆是否为空"""
        return self.size() == 0
    
    def swap(self, i, j):
        self.max_heaap[i], self.max_heaap[j] = self.max_heaap[j], self.max_heaap[i]
    
    def peek(self):
        """访问堆顶元素"""
        return self.max_heap[0]
    
    def push(self, val):
        self.max_heaap.append(val)
        self.sift_up(self.size() - 1)
    
    def sift_up(self, i):
        """从节点 i 开始，从底至顶堆化"""
        while True:
            p = self.parent(i)
             # 当“越过根节点”或“节点无须修复”时，结束堆化
            if p < 0 or self.max_heaap[i] <= self.max_heap[p]:
                break
            self.swap(i, p)
            i = p
    
    def pop(self):
        """出堆"""
        if self.is_empty():
            raise IndexError("堆为空")
        # 交换根节点与最右叶节点(交换首元素与尾元素)
        self.swap(0, len(self.max_heaap) - 1)
        val = self.max_heaap.pop()
        # 从顶至底对话
        self.sift_down(0)
        # 返回堆顶元素
        return val
    
    def sift_down(self, i):
        """从节点 i 开始，从顶至底堆化"""
        while True:
            # ma 记为最大值的节点,必须左右节点都要遍历一遍，不要用elif
            l, r, ma = self.left(i), self.right(i), i
            if l < self.size() and self.max_heaap[l] > self.max_heap[ma]:
                ma = l
            if r < self.size() and self.max_heaap[r] > self.max_heap[ma]:
                ma = r

            # 若 ma 等于 i，说明左右子节点都不比根节点大，则结束
            if ma == i:
                break
            self.swap(i, ma)
            # 循环向下堆化
            i = ma
            
        

""""Driver Code"""
if __name__ == "__main__":
    # 初始化大顶堆
    # 请注意，输入数组已经是一个已经是一个合法的堆 
    max_heap = [9, 8, 6, 6, 7, 5, 2, 1, 4, 3, 6, 2]

    # 获取堆顶元素
    peek = max_heap.peek()
    print(f"对顶元素为 {peek}")

    # 元素入堆
    val = 7
    max_heap.push(val)


    # 请注意，输入数组已经是一个已经是一个合法的堆
    max_heap = MaxHeap([9, 8, 7, 6, 7, 6, 2, 1, 4, 3, 6, 2, 5])

    # 堆顶元素出堆
    peek = max_heap.pop()  #pop()用于删除并返回列表中的一个元素（默认为最后一个元素）



