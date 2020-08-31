class Solution:
    def findNumbers(self, nums):
        count,result = 0, 0
        for i in nums:
            count = len(str(i))
            if (count % 2 == 0):
                result = result + 1
        return result

a = [123, 234, 12, 5678,345665]
sol = Solution()
print (sol.findNumbers(a))
