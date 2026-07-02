class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        cur_str = ""
        for digit in digits:
            cur_str += str(digit)
        new_number = int(cur_str) + 1
        res = []
        for digit in str(new_number):
            res.append(int(digit))
        return res
        