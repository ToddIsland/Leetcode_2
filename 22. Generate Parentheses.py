class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def iter(str, left):
            if len(str) == n * 2:
                if left == 0:
                    res.append(str)
                return

            if left > 0:
                iter(str + "(", left + 1)
                iter(str + ")", left - 1)
            else:
                iter(str + "(", left + 1)

        iter("", 0)

        return res
