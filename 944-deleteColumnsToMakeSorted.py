# https://leetcode-cn.com/problems/delete-columns-to-make-sorted/
class Solution(object):
    def minDeletionSize(self, A):
    	if len(A) == 0: return 0;
    	length = len(A[0]);
    	unsorted = 0;
    	for i in range(0, length):
    		x = "";
    		for j in range(0,len(A)):
    			if j == 0:
    				x = A[j][i];
    			else:
    				y = A[j][i];
    				if x > y:
    					unsorted += 1;
    					break;
    				else:
    					x = y;
    	return unsorted;

aa = Solution();
print(aa.minDeletionSize(["rrjk","furt","guzm"]))