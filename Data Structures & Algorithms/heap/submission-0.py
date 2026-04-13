class MinHeap:
    
    def __init__(self):
        self.heap = [0] # intialise heap with a dummy value at index 0 REMEMBER FIRST VALUE IS AT INDEX 1 SO THE MATHS CHECKS OUT
        

    def push(self, val: int) -> None:
        """ Append the value to the heap. Then perlocate up. """
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1) # why is it -1


    def pop(self) -> int:
        """ Swap the value of the root with the right-most element of the last level of the heap.
        Can then delete the last value of heap.
        Percolate the swapped value down until it reaches the right place  """
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop() # because heap is implemented as an array .pop() removes last element (bottom of the tree)
        root = self.heap[1]
        # last element = root
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return root
        



        

    def top(self) -> int:
        """Returns the smallest value without popping it."""
        return self.heap[1] if len(self.heap) > 1 else -1
        

    def heapify(self, nums: List[int]) -> None:
        """ The heapify algorithm converts an array to heap
        First it adds a [0] to start so that the first element is at index 1.
         It works on the basis half of the array (heap) will always be a leaf 
        The algorithm only goes through and put each node(with leaves) (starting with the bottom most) in the right place using bubble down. """
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)



    
    def _bubble_up(self, index):
        """ check if parent is bigger than index if so swap move the index upwards to the parent and calculate a new parent 
            index - candidate to replace parent 
            parent - parent node 
            during the process they swap and index > parent so index > root"""
        
        parent = index // 2
        # index > 1 = index is greater than the root and swap if parent > root for min heap
        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
            index = parent
            parent = index // 2
    
    def _bubble_down(self,index):
        """
        Move a node downward until heap property is satisfied.

        At each step:
        - Compare with left and right child
        - Swap with the smaller child
        """

        while 2 * index < len(self.heap):

            left_child = 2 * index
            right_child = 2 * index + 1

            smallest = left_child

            if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child]:
                smallest = right_child

            if self.heap[index] <= self.heap[smallest]:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
                


            


        
        