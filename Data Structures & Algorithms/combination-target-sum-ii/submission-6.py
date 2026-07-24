class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []
        subset = []

        def backtracking(start, current_sum):

            if current_sum == target:
                result.append(subset.copy())
                return
            
            for i in range(start, len(candidates)):
                number = candidates[i]

                if current_sum + number > target:
                    break
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                subset.append(number)

                backtracking(i + 1, current_sum + number)

                subset.pop()
            
        backtracking(0,0)
        return result
                