class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        nums1.extend(nums2)
        nums1.sort()
        for i in nums1:
            if (i == 0):
                print(nums1)
                nums1.remove(i)
            print(nums1)

num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3
sol = Solution()
print (sol.merge(num1, m, num2, n))

