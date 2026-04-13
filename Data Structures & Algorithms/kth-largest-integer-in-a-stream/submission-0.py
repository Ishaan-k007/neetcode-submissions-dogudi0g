class KthLargest:
    """ We want the k-th largest number in a stream of values.
    The simplest approach:
    Every time a new value comes in, insert it, sort the list, and then pick the element at position len(arr) - k."""

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

        

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]
        
