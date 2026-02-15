# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. 
# Test cases are generated so that the answer will fit in a 32-bit integer.

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        numSum = 0

        nums = []
        curr_num = []

        def dfs(node, curr_num):

            if not node:
                return
            
            curr_num.append(str(node.val))

            if not node.left and not node.right:
                nums.append(curr_num[:])
            else:
                dfs(node.left, curr_num)
                dfs(node.right, curr_num)
            curr_num.pop()
        
        dfs(root, [])

        for num in nums:
            num = int("".join(num))
            numSum += num

        return numSum
        