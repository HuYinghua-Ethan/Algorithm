"""
从物理结构的角度来看，树是一种基于链表的数据结构，因此其遍历方式是通过指针逐个访问节点。
然而，树是一种非线性结构，这使得遍历树比遍历链表更加复杂，需要借助搜索算法来实现。

二叉树常见的遍历方式包括层序遍历、前序遍历、中序遍历和后序遍历等


"""



"""
层序遍历从顶部到底部逐层遍历二叉树，并在每一层按照从左到右的顺序访问节点。
层序遍历本质上属于广度优先遍历，也成为广度优先搜索（BFS），它体现了一种“一圈一圈向外拓展”的逐层遍历方式。
广度优先遍历通常借助“队列”来实现。队列遵循“先进先出”的规则，而广度优先遍历则遵循“逐层推进”的规则，两者背后的思想是一致的。
"""
# 代码实现 

from collections import deque 





class TreeNode:
    """二叉树节点类"""
    def __init__(self, val):
        self.val = val                      # 节点值
        self.left:TreeNode | None = None    # 左子节点引用
        self.right:TreeNode | None = None   # 右子节点引用


 
def list_to_tree_dfs(arr, i):
    """将列表反序化为二叉树：递归"""
    # 如果索引超出数组长度，或者对应的元素为 None ，则返回 None
    if(i < 0 or i >= len(arr) or arr[i] is None):  # 跳出递归的条件
        return None
    # 构建当前节点
    root = TreeNode(arr[i])
    # 递归构建左右子树
    root.left = list_to_tree_dfs(arr, i * 2 + 1)
    root.right = list_to_tree_dfs(arr, i * 2 + 2)
    return root  # 返回根节点


def list_to_tree(arr):
    """将列表反序化为二叉树"""
    return list_to_tree_dfs(arr, 0)


def levelOrder(root):
    res = []
    queue = deque()
    queue.append(root)
    print("queue :", queue)
    while queue:
        node = queue.popleft()  # 从左到右取出队列的值
        res.append(node.val)
        if node.left is not None:  # 若左子节点不为空，则添加到队列中
            queue.append(node.left)
        if node.right is not None: # 若右子节点不为空，则添加到队列中
            queue.append(node.right)
    return res
            
        

"""前序、中序和后序遍历都属于深度优先遍历，也称深度优先搜索，它体现了一种“先走到尽头，再回溯继续”的遍历方式。"""
def pre_order(root):
    """前序遍历"""
    if root is None:
        return

    # 访问优先级：根节点->左节点->右节点
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)


def in_order(root):
    """中序遍历"""
    if root is None:
        return
    
    # 访问优先级：左节点->根节点->右节点
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)


def post_order(root):
    """后序遍历"""
    if root is None:
        return
    
    # 访问优先级：左节点->右节点->根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)


"""Driver Code"""
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = list_to_tree(arr)
    
    res = []
    res = levelOrder(root)
    print("\n层序遍历的节点打印序列 = ", res)

    # 前序遍历
    res.clear()
    pre_order(root)
    print("\n前序遍历的节点打印序列 = ", res)

    # 中序遍历
    res.clear()
    in_order(root)
    print("\n中序遍历的节点打印序列 = ", res)

    # 后序遍历
    res.clear()
    post_order(root)
    print("\n后序遍历的节点打印序列 = ", res)
    


    