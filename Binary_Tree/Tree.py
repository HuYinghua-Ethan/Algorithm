"""
二叉树是一种非线性数据结构，代表“祖先”和“后代”之间的派生关系，体现了“一分为二”的分治逻辑。
与链表类似，二叉树的基本单元是节点，每个节点包含值、左节点引用和右节点引用。

每个节点都有两个引用(指针),分别指向左子节点和右子节点，该节点被称为这两个子节点的父节点。
当给定一个二叉树的节点时，我们将该节点的左子节点及其以下节点形成的树称为该节点的左子树，右子节点及其以下节点形成的树称为该节点的右子树。

在二叉树中，除叶节点外，其他所有节点都包含子节点和非空子树。

"""

class TreeNode:
    def __init__(self, val):
        self.val = val                      # 节点值
        self.left:TreeNode | None = None    # 左子节点引用
        self.right:TreeNode | None = None   # 右子节点引用


""""Driver Code"""
if __name__ == "__main__":

    # 初始化节点
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    
    # 构建节点之间的引用
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5














