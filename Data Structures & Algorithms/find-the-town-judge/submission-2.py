class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trustee = []
        trusted = []

        for relation in trust:
            trustee.append(relation[0])
            trusted.append(relation[1])
        
        judge = trusted[0]

        if len(set(trusted)) == 1:
            if len(trusted) == len(trustee):
                if judge not in trustee:
                    return judge
        return -1  
        