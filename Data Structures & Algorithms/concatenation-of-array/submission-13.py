class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.ans=tuple(nums)*2
        return list(self.ans)