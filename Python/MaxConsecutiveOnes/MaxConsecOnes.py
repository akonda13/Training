class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        result, counter = 0, 0

        for i in nums:
            if (i == 1):
                counter = counter + 1
            else:
                counter = 0
            result = max(result,counter)
        return result

a = [1,0,1,1,1,0,1]
sol = Solution()
print (sol.findMaxConsecutiveOnes(a))
