# We can use backtracking to solve the Subsets problem because the solution space, all possible combinations of elements forms a power set, which grows exponentially with the number of elements. 
# For n elements, there are 2^n subsets. Backtracking is a natural fit because it allows us to systematically explore all combinations by including or excluding each element, without needing to generate all combinations manually.


from typing import List

def subsets(nums):
    res = []

    def backtrack(idx, subset):
        if idx < 0:
            res.append(subset[:])
            return
        subset.append(nums[idx])
        backtrack(idx-1, subset)
        subset.pop()
        backtrack(idx-1, subset)
    backtrack(len(nums)-1, [])

    return res

print(subsets([2, 4, 3])) 