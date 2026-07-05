class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        
        def backtrack(i,subset):
            nonlocal res
            
            if i == len(s):
                res.append(list(subset))
                return
            
            for j in range(i,len(s)):
                cur_slice = s[i:j+1]
                if cur_slice[::-1] == cur_slice:
                    subset.append(cur_slice)
                    backtrack(j+1,subset)
                    subset.pop()


        backtrack(0,[])
        return res

