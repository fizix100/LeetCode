# https://leetcode-cn.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        map = [];
        for x in range(0,m):
        	list = [];
        	map.append(list);
        	for y in range(0,n):
        		if x > 0 and y > 0:
        			list1 = map[x-1];
        			list2 = map[x];
        			list.append(list1[y] + list2[y-1]);
        		else:
        			list.append(1);
        return (map[m-1][n-1]);
