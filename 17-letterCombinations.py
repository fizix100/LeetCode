#https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        phone = ["", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"];
        result = [];
        currentLen = 0;
        for x in digits:
        	currentLen += 1;
        	letters = list(phone[int(x)-1]);
        	if len(result) == 0:
        		result.extend(letters);
        	else:
        		newResult = [];
        		for y in letters:
        			for i in range(0,len(result)):
        				newResult.append(result[i] + y);
        		result = newResult;
        return result;