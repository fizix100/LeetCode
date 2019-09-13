# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
class Solution(object):
    def sumNumbers(self, root):
        if root is None: return 0;

        stack = [root];
        result = 0;
        while len(stack) > 0:
        	node = stack.pop();
        	if node.left is None and node.right is None:
        		result += node.val;
        	else:
	        	if node.left:
	        		left = node.left;
	        		left.val = int(str(node.val) + str(left.val));
	        		stack.append(left);
	        	if node.right:
	        		right = node.right;
	        		right.val = int(str(node.val) + str(right.val));
	        		stack.append(right);
        return result;
