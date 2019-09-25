# https://leetcode-cn.com/problems/assign-cookies/
class Solution(object):
    def findContentChildren(self, g, s):
        result = 0;
        g.sort();
        s.sort();
        
        for m in range(0, len(s)):
        	x = s[m];
        	n = 0;
        	found = False;
        	while n < len(g) and found == False:
        		y = g[n];
        		if n == 0 and x < y:
        			break;
        		if x == y or (x >= y and (n == len(g)-1 or x < g[n+1])):
        			result += 1;
        			g.remove(y);
        			found = True;
        		else:
        			n +=1;
        return result;
