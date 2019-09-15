# https://leetcode-cn.com/problems/count-primes/
import cmath

class Solution(object):
    def countPrimes(self, n):
    	if n < 3: return 0;

    	result = [2,3,5];
    	if n < 7:
    		rs = [];
    		for x in xrange(2,n):
    			if result.count(x) > 0:
    				rs.append(x);
    		return len(rs);
    	else:
	        for x in xrange(6,n,6):
	        	a = x + 1;
	        	b = x + 5;
	        	mark = int(cmath.sqrt(b).real) + 1
	        	isA = True;
	        	if a >= n: continue;
	        	for y in result:
	        		if y >= mark:
	        			break;
	        		if a % y == 0:
	        			isA = False;
	        			break;
	        	if isA:
	        		result.append(a);

	        	if b >= n: continue;
	        	isA = True;
	        	for y in result:
	        		if y >= mark:
	        			break;
	        		if b % y == 0:
	        			isA = False;
	        			break;
	        	if isA:
	        		result.append(b);
	    	return len(result);