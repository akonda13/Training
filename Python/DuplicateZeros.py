class Solution:
    def duplicateZeros(self, arr):
        # n = len(arr)
        # i = 0
        # while i<n:
        #     if (arr[i] == 0):
        #         arr.insert(i+1, 0)
        #         arr.pop();
        #         i = i+2;
        #     else:
        #         i = i+1

        n = len(arr)-1
        for i in range(n, -1,-1): # start,stop,step
            if arr[i] == 0:
                del arr[-1]
                arr.insert(i+1, 0)
        print (arr)

a = [1,0,2,3,0,4,5,0]
sol = Solution()
print (sol.duplicateZeros(a))

