class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def backtrack(i,subset,k):
            nonlocal res

            if len(subset) == k:
                res.append(subset[:])
                return




            for j in range(i,n+1):
                subset.append(j)
                backtrack(j+1,subset,k)
                subset.pop()

        backtrack(1,[],k)
        return res




            
        