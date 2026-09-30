class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    # Якщо дерево порожнє,
    # повертаємо None
    if root is None:
        return None

    # Міняємо місцями ліве та праве піддерева
    root.left, root.right = root.right, root.left

    # Інвертуємо ліве піддерево
    invertTree(root.left)

    # Інвертуємо праве піддерево
    invertTree(root.right)

    return root


def treeToList(root):
    """
    Перетворює дерево у список
    для зручного виведення результату.
    """

    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node is None:
            result.append(None)
            continue

        result.append(node.val)

        queue.append(node.left)
        queue.append(node.right)

    # Видаляємо зайві None з кінця списку
    while result and result[-1] is None:
        result.pop()

    return result


# ==========================================
# ТЕСТУВАННЯ
# ==========================================

# Приклад 1:
# Input:  [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

root1 = TreeNode(4)

root1.left = TreeNode(2)
root1.right = TreeNode(7)

root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)

print("Приклад 1:", treeToList(invertTree(root1)))


# Приклад 2:
# Input:  [2,1,3]
# Output: [2,3,1]

root2 = TreeNode(2)

root2.left = TreeNode(1)
root2.right = TreeNode(3)

print("Приклад 2:", treeToList(invertTree(root2)))


# Приклад 3:
# Input:  []
# Output: []

root3 = None

print("Приклад 3:", treeToList(invertTree(root3)))