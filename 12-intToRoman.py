#https://leetcode-cn.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        numPad = {1:"I",5:"V",9:"IX",10:"X",50:"L",90:"XC",100:"C",500:"D",900:"CM",1000:"M"};
        keys = [1000,900,500,100,90,50,10,9,5,1];
        numbers = [];
        for x in keys:
        	numbers.append(num//x);
        	num %=x;
        result = "";
        for i in range(0,len(numbers)):
        	x = numbers[i];
        	if x > 0 and x < 4:
        		result = result + (numPad[keys[i]] * x);
        	elif x == 4:
        		result = result + (numPad[keys[i]] + numPad[keys[i-1]]);
        return result;


aa = Solution();
aa.intToRoman(3899);