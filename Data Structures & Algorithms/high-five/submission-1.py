class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        # created a dictionary that maps to a list
        all_scores = defaultdict(list)

        for item in items:
            student_id = item[0]
            value = item[1]

            heapq.heappush(all_scores[student_id], -value)

        solution = []

        for student_id in sorted(all_scores.keys()):
            avg_score = 0
            for i in range(5):
                avg_score += -heapq.heappop(all_scores[student_id])
            avg_score = avg_score // 5
            solution.append([student_id, avg_score])
        
        return solution
          
        
        