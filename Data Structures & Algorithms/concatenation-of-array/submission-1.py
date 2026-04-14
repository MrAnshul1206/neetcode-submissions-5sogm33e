class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            ans.append(x)    # pehla copy
        for x in nums:
            ans.append(x)    # doosra copy
        return ans
