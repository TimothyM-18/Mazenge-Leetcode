from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nums):
    if not nums:
        return None
    
    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nums):
        node = queue.popleft()

        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1

        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root

print(build_tree([1,2,3,4,5,6,8]))


