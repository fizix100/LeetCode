# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
class Solution(object):
    def levelOrder(self, root):
        if root is None: return [];
        result = [];
        stack1 = [root];
        stack2 = [];
        while len(stack1) or len(stack2) > 0:
        	level = [];
        	if len(stack1) > 0:
        		while len(stack1) > 0:
        			node = stack1.pop(0);
        			level.append(node.val);
        			if node.left:
        				stack2.append(node.left);
        			if node.right:
        				stack2.append(node.right);
        	elif len(stack2) > 0:
        		while len(stack2) > 0:
        			node = stack2.pop(0);
        			level.append(node.val);
        			if node.left:
        				stack1.append(node.left);
        			if node.right:
        				stack1.append(node.right);
        	result.append(level);
        return result;