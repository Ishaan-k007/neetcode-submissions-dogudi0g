# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        middle = len(pairs) // 2
        left = self.mergeSort(pairs[:middle])
        right = self.mergeSort(pairs[middle:])

        return self.merge(left, right)

    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        L = 0
        R = 0
        sorted_list = []

        while L < len(left) and R < len(right):
            if left[L].key <= right[R].key:
                sorted_list.append(left[L])
                L += 1
            else:
                sorted_list.append(right[R])
                R += 1

        # Add remaining elements from left or right
        sorted_list.extend(left[L:])
        sorted_list.extend(right[R:])

        return sorted_list


