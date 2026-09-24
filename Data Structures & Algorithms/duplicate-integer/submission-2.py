class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:      # 1. have I seen this before?
                return True    # 2. yes -> duplicate, stop immediately
            seen.add(n)        # 3. no -> remember it, keep going
        return False           # got through everything, no repeats