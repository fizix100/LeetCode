class Solution(object):
    def singleNumber1(self, nums):
        nums.sort();
        x = 0;
        while x < len(nums):
        	if x == len(nums)-1:
        		return nums[x];
        	elif nums[x] != nums[x+1]:
        		return nums[x];
        	else:
        		x = x+2;
    def singleNumber2(self, nums):
        map = {};
        for x in nums:
        	if map.has_key(x) == False:
        		map[x] = 0;
        	else:
        		map.pop(x);
        return map.keys()[0];
    def singleNumber3(self, nums):
        result = 0;
        for x in nums:
        	result = result ^ x;
        return result;
    def singleNumber(self, nums):
        return sum(set(nums))*2 - sum(nums);

aa = Solution();
print(aa.singleNumber([4,1,2,1,2]));