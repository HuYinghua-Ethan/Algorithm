"""
给定一棵完美二叉树，我们将所有节点按照层序遍历的顺序存储在一个数组中，则每个节点都对应唯一的数组索引。

根据层序遍历的特性，我们可以推导出父节点索引与子节点索引之间的“映射公式”：若某节点的索引为 i ，则该节点的左子节点索引为 2i+1 ，右子节点索引为 2i+2 


完全二叉树非常适合使用数组来表示。回顾完全二叉树的定义，None 只出现在最底层且靠右的位置，因此所有 None 一定出现在层序遍历序列的末尾。


以下代码实现了一棵基于数组表示的二叉树，包括以下几种操作。
1.给定某节点，获取它的值、左（右）子节点、父节点。
2.获取前序遍历、中序遍历、后序遍历、层序遍历序列。

"""

class TreeNode:
    """二叉树节点类"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ArrayBinaryTree:
    """数组表示下的二叉树类"""

    def __init__(self, arr: list[int | None]):
        """构造方法"""
        self._tree = list(arr)

    def size(self):
        """列表容量"""
        return len(self._tree)

    def val(self, i: int) -> int:
        """获取索引为 i 节点的值"""
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        """获取左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        """获取右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        """获取父节点的索引"""
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        # 直接遍历数组
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str):
        """深度优先遍历"""
        if self.val(i) is None:
            return
        # 前序遍历
        if order == "pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)
        # 中序遍历
        if order == "in":
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)
        # 后序遍历
        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        """前序遍历"""
        self.res = []
        self.dfs(0, order="pre")
        return self.res

    def in_order(self) -> list[int]:
        """中序遍历"""
        self.res = []
        self.dfs(0, order="in")
        return self.res

    def post_order(self) -> list[int]:
        """后序遍历"""
        self.res = []
        self.dfs(0, order="post")
        return self.res

"""Driver Code"""
if __name__ == "__main__":
    # 初始化二叉树
    arr = [1, 2, 3, 4, None, 6, None]
    abt = ArrayBinaryTree(arr)

    # 访问节点
    i = 1
    l, r, p = abt.left(i), abt.right(i), abt.parent(i)

    # 遍历树
    res = abt.level_order()
    res = abt.pre_order()
    res = abt.in_order()
    res = abt.post_order()




"""
二叉树的数组表示主要有以下优点:
1.数组存储在连续的内存空间中，对缓存友好，访问与遍历速度较快。
2.不需要存储指针，比较节省空间。
3.允许随机访问节点。


然而，数组表示也存在一些局限性:
1.数组存储需要连续内存空间，因此不适合存储数据量过大的树。
2.增删节点需要通过数组插入与删除操作实现，效率较低。
3.当二叉树中存在大量 None 时，数组中包含的节点数据比重较低，空间利用率较低。

"""






