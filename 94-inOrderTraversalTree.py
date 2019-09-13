# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# 递归
class Solution(object):
    def inorderTraversal(self, root):
    	result = [];
        if root is None:
        	return result;
        if root.left:
        	result.extend(self.inorderTraversal(root.left));
        result.append(root.val);
        if root.right:
        	result.extend(self.inorderTraversal(root.right));
        return result;

# 迭代
class Solution(object):
    def inorderTraversal(self, root):
    	result = [];
    	stack = [];
    	node = root;
    	while node or len(stack) > 0:
    		if node:
    			stack.append(node);
    			node = node.left;
    		else:
    			node = stack.pop();
    			result.append(node.val);
    			node = node.right;
    	return result;