class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Does current char match?
            match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            # Next char is '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                # Option 1: use zero occurrences
                # Option 2: use one occurrence and stay on same pattern char
                memo[(i, j)] = (
                    dfs(i, j + 2)
                    or (match and dfs(i + 1, j))
                )
            else:
                # Normal character / '.'
                memo[(i, j)] = match and dfs(i + 1, j + 1)

            return memo[(i, j)]

        return dfs(0, 0)
        