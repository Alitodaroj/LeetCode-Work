class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        sum_original = N *  (N + 1) / 2
        sum_given = sum(nums)

        return int(sum_original - sum_given)