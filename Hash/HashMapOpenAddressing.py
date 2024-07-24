""""
开放寻址不引入额外的数据结构，而是通过“多次探测”来处理哈希冲突。
探测方式主要包括线性探测、平方探测和多次哈希等。


1.线性探测
线性探测采用固定步长的线性搜索来进行探测，其操作方法与普通哈希有所不同。
插入元素：通过哈希函数计算桶索引，若发现桶内已有元素，则从冲突位置向后线性遍历(步长通常为1)，直至找到空桶，将元素插入其中
查找元素：若发现哈希冲突，则使用相同步长向后进行线性遍历，直到找到对应元素，返回value即可；
如果遇到空桶，说明目标元素不再哈希表，返回 None。

根据此哈希函数，最后两位相同的 key 都会被映射到相同的桶。而通过线性探测，它们被依次存储在该桶以及之下的桶中。

然而，线性探测容易产生“聚集现象”。具体来说，数组中连续被占用的位置越长，这些连续位置发生哈希冲突的可能性越大，从而进一步促使该位置的聚堆生长，形成恶性循环，最终导致增删查改操作效率劣化。


我们不能在开放寻址哈希表中直接删除元素。这是因为删除元素会在数组内产生一个空桶 None
而当查询元素时，线性探测到该空桶就会返回，因此在该空桶之下的元素都无法再被访问到，程序可能误判这些元素不存在
为了解决该问题，我们可以采用懒删除机制：它不直接从哈希表中移除元素，而是利用一个常量 TOMBSTONE 来标记这个桶。
在该机制下，None 和 TOMBSTONE 都代表空桶，都可以放置键值对。
但不同的是，线性探测 TOMBSTONE 时应该继续遍历，因为其之下可能还存在键值对

然而，懒删除可能会加速哈希表的性能退化。这是因为每次删除操作都会产生一个删除标记，随着 TOMBSTONE 的增加，搜索时间也会增加，因为线性探测可能需要跳过多个 TOMBSTONE 才能找到目标元素。

为此，考虑在线性探测中记录遇到的首个 TOMBSTONE 的索引，并将搜索到的目标元素与该 TOMBSTONE 交换位置。
这样做的好处是当每次查询或添加元素时，元素会被移动至距离理想位置（探测起始点）更近的桶，从而优化查询效率。

以下代码实现了一个包含懒删除的开放寻址（线性探测）哈希表。为了更加充分地使用哈希表的空间，我们将哈希表看作一个“环形数组”，当越过数组尾部时，回到头部继续遍历。


2.平方探测
当发生冲突时，平方探测不是简单地跳过一个固定的步数，而是跳过“探测次数的平方”的步数，即1,4,9,...步

平方探测主要具有以下优势：
平方探测通过跳过探测次数平方的距离，试图缓解线性探测的聚集效应。
平方探测会跳过更大的距离来寻找空位置，有助于数据分布得更加均匀。

然而，平方探测并不是完美的：
仍然存在聚集现象，即某些位置比其他位置更容易被占用。
由于平方的增长，平方探测可能不会探测整个哈希表，这意味着即使哈希表中有空桶，平方探测也可能无法访问到它。

3.多次哈希
顾名思义，多次哈希方法使用多个哈希函数f1(x)、f2(x)、f3(x)...进行探测。

插入元素：若哈希函数 f1(x)出现冲突，则尝试 f2(x)，以此类推，直到找到空位后插入元素。
查找元素：在相同的哈希函数顺序下进行查找，直到找到目标元素时返回；若遇到空位或已尝试所有哈希函数，说明哈希表中不存在该元素，则返回 None 。
与线性探测相比，多次哈希方法不易产生聚集，但多个哈希函数会带来额外的计算量。


"""

class Pair:
    """键值对"""
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashMapOpenAddressing:
    """开放寻址哈希表"""
    def __init__(self):
        self.size = 0      # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]   # 桶数组
        self.TOMESTONE = Pair(-1, "-1")  # 删除标记

    def hash_func(self, key):
        """哈希函数"""
        return key % self.capacity
    
    def load_factor(self):
        """负载因子"""
        return self.size / self.capacity

    def find_bucket(self, key):
        """搜索 key 对应的桶索引"""
        index = self.hash_func(key)
        first_tombstone = -1
        # 线性探测，当遇到空桶时跳出
        while self.buckets[index] is not None:
            # 若遇到 key ，返回对应的桶索引
            if self.buckets[index].key == key:
                # 若之前遇到了删除标记，则将键值对移动至该索引处
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMESTONE
                    return first_tombstone    # 返回移动后的桶的索引
                return index # 返回桶索引
            if first_tombstone == -1 and self.buckets[index] == self.TOMESTONE:
                first_tombstone = index
            index = (index + 1) % self.capacity
        return index if first_tombstone == -1 else first_tombstone

            
        
    def get(self, key):
        """查询操作"""
        # 搜索 key 对应的桶索引
        index = self.find_bucket(key)
        # 若找到键值对，则返回对应 val
        if self.buckets[index] not in [None, self.TOMESTONE]:
            return self.buckets[index].val
        # 若键值对不存在，则返回 None
        return None         

            
    def put(self, key, val):
        """添加操作"""
        if self.load_factor() > self.load_thres:
            self.extend()  # 若负载因子超过阈值，则扩容
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMESTONE]:
                self.buckets[index].val = val  # 更新 val
                return
        self.buckets[index] = Pair(key, val)
        self.size += 1
      
    def remove(self, key):
        """删除操作"""
        # 搜索 key 对应的桶索引
        index = self.find_bucket(key)
        # 若找到键值对，则用删除标记覆盖它
        if self.buckets[index] not in [None, self.TOMESTONE]:
            self.buckets[index] = self.TOMESTONE
            self.size -= 1
            
    def extend(self):
        """"扩容哈希表"""
        # 暂存原哈希表
        buckets_temp = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        # 将键值对从原哈希表中搬至新哈希表
        for pair in buckets_temp:
            if pair not in [None, self.TOMESTONE]:
                self.put(pair.key, pair.val)
        













