class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 

        

    def sumRange(self, left: int, right: int) -> int:
        new_arr = [0] * len(self.nums)
        new_arr[0] = self.nums[0]
        current_sum = self.nums[0]
        for i in range(1,len(self.nums)):
            current_sum += self.nums[i]
            new_arr[i] = current_sum
        print(new_arr)

        if left == 0:
            return new_arr[right]
        return new_arr[right] - new_arr[left - 1]
 

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)