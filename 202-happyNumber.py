# https://leetcode-cn.com/problems/happy-number/
class Solution(object):
    def isHappy(self, n):
        a = [];
        while n!=1 and a.count(n) == 0:
        	a.append(n);
        	string = str(n);
        	result = 0;
        	for x in range(0,len(string)):
        		result += pow(int(string[x]),2);
        	n = result;
        return n==1;