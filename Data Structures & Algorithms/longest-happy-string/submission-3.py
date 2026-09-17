import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # scheduling problem
        # each time has the max letter in a heap
        # puts too then puts it into cooldown
        # repeats untill the heap is empty
        # if the heap is empty and something is in the cooldown then cant do it return count


        heap = []
        if a > 0:
            heapq.heappush(heap,[-a,"a"])
        if b > 0:
            heapq.heappush(heap,[-b,"b"])
        if c > 0:
            heapq.heappush(heap,[-c,"c"])

        print(heap)

        prev_letter = ""
        prev_freq = 0
        res = ""
        while heap:
            freq , letter = heapq.heappop(heap)
            freq = -freq

            # 2 letters same before
            if len(res) >= 2:
                if letter == res[-1] == res[-2]:
                    prev_letter = letter
                    prev_freq = freq
                    if heap:
                        freq , letter = heapq.heappop(heap)
                        freq = -freq
                        heapq.heappush(heap,[-prev_freq,prev_letter])
                    else:
                        return res
            res += letter
            freq -= 1

            if freq > 0:
                heapq.heappush(heap,[-freq,letter])

            
            

            
        return res

