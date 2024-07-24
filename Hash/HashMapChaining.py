"""
通常情况下哈希函数的输入空间远大于输出空间，因此，哈希冲突是不可避免的。
哈希冲突会导致查询结果错误，严重影响哈希表的可用性。
解决哈希冲突可以采用以下策略：
1.改良哈希表数据结构，使得哈希表可以在出现哈希冲突时正常工作
2.仅在必要时，即当哈希冲突比较严重时，才执行扩容操作

哈希表的结构改良方法主要包括“链式地址”和“开放寻址”

在原始哈希表中，每个桶仅能存储一个键值对。
链式地址将单个元素转换为链表，将键值对作为链表节点，将所有发生冲突的键值对都存储在同一链表中

基于链式地址实现的哈希表的操作方法发生了以下变化：
查询元素：输入 key ，经过哈希函数得到桶索引，即可访问链表头节点，然后遍历链表并对比 key 以查找目标键值对。
添加元素：首先通过哈希函数访问链表头节点，然后将节点（键值对）添加到链表中。
删除元素：根据哈希函数的结果访问链表头部，接着遍历链表以查找目标节点并将其删除。


链式地址存在以下局限性：
占用空间增大：链表包含节点指针，它相比数组更加耗费内存空间。
查询效率降低：因为需要线性遍历链表来查找对应元素。

以下代码需要注意两点：
使用列表（动态数组）代替列表，从而简化代码。在这种设定下，哈希表（数组）包含多个桶，每个桶都是一个列表
当负载因子超过 2/3 时，我们将哈希表扩容至原先的2倍


"""



class Pair:
    """键值对"""
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashMapChaining:
    """链式地址哈希表"""
    def __init__(self):
        """构造方法"""
        self.size = 0      # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]   # 桶数组


    def hash_func(self, key):
        """哈希函数"""
        return key % self.capacity
    
    def load_factor(self):
        """负载因子"""
        return self.size / self.capacity
    
    def get(self, key):
        """查询操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return None
    
    def put(self, key, val):
        """添加操作"""
        if self.load_factor() > self.load_thres:  # 如果负载因子大于设定的阈值，则扩容
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:   # 若有对应的键
                pair.val = val    # 则添加对应的值
                return
        pair = Pair(key, val)     # 如果都没有，则把新的键值对添加到桶中
        bucket.append(pair)
        self.size += 1            # 更新键值对的数量
        
    def remove(self, key): 
        """删除操作"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break
    
    def extend(self):
        """扩容哈希表"""
        buckets = self.buckets  # 首先保存当前的桶数组
        self.capacity *= self.extend_ratio  # 扩大哈希表的容量
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in buckets:    # 把之前桶数组的键值对添加回扩容后的桶数组
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        """打印哈希表"""
        result = []
        for bucket in self.buckets:
            for pair in bucket:
                result.append(str(pair.key) + "->" + pair.val)
            print(result)
                


"""Driver Code"""
if __name__ == "__main__":
    # 初始化哈希表
    hashmap = HashMapChaining()

    # 添加操作
    hashmap.put(12836, "小哈")
    hashmap.put(15937, "小啰")
    hashmap.put(16750, "小算")
    hashmap.put(13276, "小法")
    hashmap.put(10583, "小鸭")
    
    # 查询操作
    name = hashmap.get(13276)
    print(name)

    # 删除操作
    hashmap.remove(12836)

    hashmap.print()



"""
值得注意的是，当链表很长时，查询效率 O(n) 很差。此时可以将链表转换为“AVL 树”或“红黑树”，从而将查询操作的时间复杂度优化至 O(log n)。
"""







