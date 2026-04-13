class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        L = 0 
        R = 0
        s = sorted(s)
        g = sorted(g)
        length = len(g)

        happy = 0

        while L < length and R < len(s) :
            
            if g[L] - s[R] <= 0:
                happy += 1
            else:
                
                while g[L] - s[R] >= 0 and R < len(s) - 1:
                    print("HI")
                    R += 1
                    if g[L] - s[R] <= 0:

                        happy += 1
                        break



            L += 1
            R += 1
        return happy


        