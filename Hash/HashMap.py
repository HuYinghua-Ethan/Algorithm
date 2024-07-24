"""
哈希表(hash table)，又称散列表，它通过建立键 key 与值 value 之间的映射，实现高效的元素查询。
在哈希表中，我们将数组中的每个空位称为桶，每个桶可存储一个键值对。
因此，查询操作就是找到 key 对应的桶，并在桶中获取 value 。

这是通过哈希函数（hash function）实现的。哈希函数的作用是将一个较大的输入空间映射到一个较小的输出空间。
在哈希表中，输入空间是所有 key ，输出空间是所有桶（数组索引）。
换句话说，输入一个 key ，我们可以通过哈希函数得到该 key 对应的键值对在数组中的存储位置。

输入一个 key ，哈希函数的计算过程分为以下两步。

1.通过某种哈希算法 hash() 计算得到哈希值。
2.将哈希值对桶数量（数组长度）capacity 取模，从而获取该 key 对应的数组索引 index 。

"""


class Pair:
    """键值对"""
    def __init__(self, key, val):
        self.key = key
        self.val = val

class ArrayHashMap:
    """基于数组实现的哈希表"""
    def __init__(self):
        self.buckets = [None] * 100

    def hash_func(self, key):
        """哈希函数"""
        index = key % 100
        return index
    
    def get(self, key):
        """查询操作"""
        index = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val
        
    def put(self, key, val):
        """添加操作"""
        pair = Pair(key, val)
        index = self.hash_func(key)
        self.buckets[index] = pair
        
    def remove(self, key):
        """删除操作"""
        index = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self):
        """获取所有键值对"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result
        
    def key_set(self):
        """获取所有键"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self):
        """"获取所有值"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result

    def print(self):
        """打印哈希表"""
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)



"""Driver Code"""
if __name__ == "__main__":
    hmap = ArrayHashMap()
    
    hmap.put(12836, "小哈")
    hmap.put(15937, "小啰")
    hmap.put(16750, "小算")
    hmap.put(13276, "小法")
    hmap.put(10583, "小鸭")

    # 查询操作
    name = hmap.get(15937)

    # 删除操作
    hmap.remove(10583)

    # 遍历哈希表
    print("\n遍历键值对 key->value")
    for pair in hmap.entry_set():
        print(pair.key, "->", pair.val)



"""
从本质上看，哈希函数的作用是将所有 key 构成的输入空间映射到数组所有索引构成的输出空间
而输入空间往往远大于输出空间，因此理论上一定存在“多个输入对应相同输出”的情况
我们将这种多个输入对应同一输出的情况称为哈希冲突（hash collision）。
哈希表容量n越大，多个 key 被分配到同一个桶中的概率就越低，冲突就越少。因此，我们可以通过扩容哈希表来减少哈希冲突。
负载因子（load factor）是哈希表的一个重要概念，其定义为哈希表的元素数量除以桶数量，用于衡量哈希冲突的严重程度，也常作为哈希表扩容的触发条件。
"""





