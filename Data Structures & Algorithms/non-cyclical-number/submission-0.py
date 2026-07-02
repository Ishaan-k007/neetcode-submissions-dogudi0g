class Solution:
    def isHappy(self, n: int) -> bool:
        set_num  = set()

        while n != 1 :
            cur_total = 0
            for digit in (str(n)):
                
                cur_total += int(digit) ** 2
            if cur_total in set_num:
                return False
            else:
                set_num.add(cur_total)
            n = cur_total
        return True


            