class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 构造测试用的二叉树
def create_test_tree():
    # 创建叶子节点
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    # 创建中间节点
    node2 = TreeNode(2, left=node4, right=node5)
    node3 = TreeNode(3, right=node6)

    # 创建根节点
    root = TreeNode(1, left=node2, right=node3)

    return root

# 前序遍历（递归）
def pre_order(root: TreeNode | None):
    if root is None:
        return []
    res = []
    res.append(root.val)
    res.extend(pre_order(root.left))
    res.extend(pre_order(root.right))
    return res

# 中序遍历（递归）
def in_order(root: TreeNode | None):
    if root is None:
        return []
    res = []
    res.extend(in_order(root.left))
    res.append(root.val)
    res.extend(in_order(root.right))
    return res

# 后序遍历（递归）
def post_order(root: TreeNode | None):
    if root is None:
        return []
    res = []
    res.extend(post_order(root.left))
    res.extend(post_order(root.right))
    res.append(root.val)
    return res

# 前序遍历（栈）
def pre_order_iterative(root: TreeNode | None) -> list:
    if root is None:
        return []
    
    stack = [root]  # 初始化栈，压入根节点
    res = []

    while stack:
        node = stack.pop()  # 弹出栈顶节点
        res.append(node.val)  # 访问根节点

        # 先压右子树，再压左子树（保证左子树先被访问）
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return res

# 中序遍历（栈）
def in_order_iterative(root: TreeNode | None) -> list:
    if root is None:
        return []
    
    stack = []
    res = []
    current = root

    while current or stack:
        # 先将当前节点的所有左子树压入栈
        while current:
            stack.append(current)
            current = current.left
        
        # 弹出栈顶节点，访问它的值
        current = stack.pop()
        res.append(current.val)
        
        # 转向右子树
        current = current.right
    
    return res

# 后序遍历（栈）
def post_order_iterative(root: TreeNode | None) -> list:
    if root is None:
        return []
    
    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        res.append(node.val)  # 先访问根节点

        # 先压左子树，再压右子树
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return res[::-1]  # 最后反转结果

# 测试遍历
if __name__ == "__main__":
    root = create_test_tree()
    print("前序遍历结果:", pre_order(root))  # 输出：[1, 2, 4, 5, 3, 6]
    print("前序遍历结果（栈）:", pre_order_iterative(root))  # 输出：[1, 2, 4, 5, 3, 6]
    print("中序遍历结果:", in_order(root))   # 输出：[4, 2, 5, 1, 3, 6]
    print("中序遍历结果（栈）:", in_order_iterative(root))   # 输出：[4, 2, 5, 1, 3, 6]
    print("后序遍历结果:", post_order(root)) # 输出：[4, 5, 2, 6, 3, 1]
    print("后序遍历结果（栈）:", post_order_iterative(root)) # 输出：[4, 5, 2, 6, 3, 1]
