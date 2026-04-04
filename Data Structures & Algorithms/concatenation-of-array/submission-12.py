class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.ans=tuple(nums)+tuple(nums)
        return list(self.ans)