class Solution:
    def reorganizeString(self, s: str) -> str:

        # put all the letters and their frequencies into a heap, ordering by frequency maxHeap
        #each time pop from heap top and reduce frequency and add the letter to the string and then add letter and frequency back to heap after a cooldown
        count = Counter(s)

        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        prev_freq = None
        prev_char = None
        res = ""
        while heap:
            print(heap)
            
            cur_freq , cur_char = heapq.heappop(heap)
            cur_freq = -cur_freq
            print(cur_freq,cur_char)

            res += cur_char

            if prev_freq:
                heapq.heappush(heap,(-prev_freq,prev_char))
                prev_freq = None
                prev_char = None

            
            if cur_freq > 1:
                prev_freq = cur_freq - 1
                prev_char = cur_char

                print("Hi",prev_freq,prev_char)
        if len(res) != len(s):
            return ""
        return res 
            
            


        