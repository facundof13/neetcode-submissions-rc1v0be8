class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        global answer
        answer = []
        
        def backtrack(path, i):
            global answer
            curr_sum = sum(path)
            if curr_sum == target:
                answer.append(path[:])
                return
            elif i >= len(nums) or curr_sum > target:
                return
            
            path.append(nums[i])
            backtrack(path, i)
            path.pop()
            backtrack(path, i + 1)

        backtrack([], 0) 
        return answer


