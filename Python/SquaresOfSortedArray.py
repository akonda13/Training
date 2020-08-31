class Solution:
    def sortedSquares(self, A):
        # result = []
        # for i in A:
        #     result.append(i*i)
        #     result.sort()
        # return result
        for i in range(len(A)):
            A[i] = A[i]*A[i]
        A.sort()
        return A

a = [-4,-1,0,3,10]
sol = Solution()
print (sol.sortedSquares(a))


