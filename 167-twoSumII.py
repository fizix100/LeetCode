#https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
class Solution(object):
    def twoSum(self, numbers, target):
    	ex = {};
        for x in range(0,len(numbers)):
        	a =  numbers[x];
        	if ex.has_key(a):
        		continue;
        	b = target - a;
        	y = -1;
        	count = numbers.count(b);
        	if count > 0:
        		y = numbers.index(b);
        		if x == y and count > 1:
        			y += 1;
        		break;
        	else:
        		ex[a] = 0;
        return [x+1, y+1];