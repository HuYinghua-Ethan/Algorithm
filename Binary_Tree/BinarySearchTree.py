"""
二叉搜索树
二叉搜索树满足以下条件：
1.对于根节点，左子树中所有节点的值 < 根节点的值 < 右子树中所有节点的值
2.任意节点的左、右子树也是二叉搜索树，即同样满足条件 1. 



1.查找节点
给定目标节点值 num ，可以根据二叉搜索树的性质来查找。如图 7-17 所示，我们声明一个节点 cur ，从二叉树的根节点 root 出发，循环比较节点值 cur.val 和 num 之间的大小关系。
若 cur.val < num ，说明目标节点在 cur 的右子树中，因此执行 cur = cur.right 。
若 cur.val > num ，说明目标节点在 cur 的左子树中，因此执行 cur = cur.left 。
若 cur.val = num ，说明找到目标节点，跳出循环并返回该节点。

2.插入节点
查找插入位置：与查找操作相似，从根节点出发，根据当前节点值和 num 的大小关系循环向下搜索，直到越过叶节点（遍历至 None ）时跳出循环。
在该位置插入节点：初始化节点 num ，将该节点置于 None 的位置。
需要注意以下两点：
(1)二叉搜索树不允许存在重复节点，否则将违反其定义。因此，若待插入节点在树中已存在，则不执行插入，直接返回。
(2)为了实现插入节点，我们需要借助节点 pre 保存上一轮循环的节点。这样在遍历至 None 时，我们可以获取到其父节点，从而完成节点插入操作。


3.删除节点
先在二叉树中查找到目标节点，再将其删除。与插入节点类似，我们需要保证在删除操作完成后，二叉搜索树的“左子树 < 根节点 < 右子树”的性质仍然满足。
因此，我们根据目标节点的子节点数量，分为0、1、2三种情况，执行对应的删除节点操作

当待删除节点的度为0时，表示该节点是叶节点，可以直接删除
当待删除节点的度为1时，将待删除节点替换为其子节点即可
当待删除节点的度为2时，我们无法直接删除它，而需要使用一个字节的替换该节点。
由于要保持二叉搜索树“左子树 < 根节点 < 右子树”的性质，因此这个节点可以是右子树的最小节点或左子树的最大节点。

假设我们选择右子树的最小节点（中序遍历的下一个节点）
1.找到待删除节点在“中序遍历序列”中的下一个节点，记为 tmp 。
2.用 tmp 的值覆盖待删除节点的值，并在树中递归删除节点 tmp 。



"""

class TreeNode:
    """二叉树节点类"""
    def __init__(self, val):
        self.val = val
        self.left:TreeNode | None = None
        self.right:TreeNode | None = None


class BinarySearchTree:
    """二叉搜索树"""
    def __init__(self):
        """初始化空树"""
        self._root = None

    def search(self, num):
        """查找节点"""
        cur = self._root
        # 循环查找，越过叶节点后跳出
        while cur is not None:
            # 目标节点在 cur 的右子树
            if cur.val < num:
                cur = cur.right
                # 目标节点在 cur 的左子树
            elif cur.val > num:
                cur = cur.left
                # 找到目标节点，跳出循环
            else:
                break
        return cur
    
    def insert(self, num):
        """插入节点"""
        if self._root is None:
            self._root = TreeNode(num)
        cur, pre = self._root, None
        while cur is not None:
            if cur.val == num:  # 若待插入节点在树中已存在，则不执行插入，直接返回。
                return  
            pre = cur   # pre 保存上一轮循环的节点，这样在遍历至 None 时，我们可以获取到其父节点，从而完成节点插入操作
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left
        # 插入节点
        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node
            
    def remove(self, num):
        if self._root is None:
            return 
        cur, pre = self._root, None
        while cur is not None:
            if cur.val == num:
                break
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left
        if cur is None:
            return
        if cur.left is None or cur.right is None:
            child = cur.left or cur.right
            if cur != self._root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                self._root = child
        else:
            temp = cur.right  # 因为遵循左子树 < 根节点 < 右子树，所以考虑右子树
            while temp.left is not None:
                temp = temp.left
            
            
            
            
            


"""Driver Code"""
if __name__ == "__main__":
    bst = BinarySearchTree()
    nums = [4, 2, 6, 1, 3, 5, 7]
    for num in nums:
        bst.insert(num)

    # 查找节点
    node = bst.search(7)
    print("\n查找到的节点对象为:{}, 节点值 = {}".format(node, node.val))
    
    














