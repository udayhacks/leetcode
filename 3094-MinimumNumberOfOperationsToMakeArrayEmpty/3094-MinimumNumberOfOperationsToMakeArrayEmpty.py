# Last updated: 04/04/2026, 13:11:17
class Solution:
    def minOperations(self, nums) -> int:
        counts = Counter(nums)
        count = 0

        for frequency in counts.values():
            if frequency == 1:
                return -1

            remainder = frequency % 3
            if remainder == 0:
                count += frequency // 3
            else:
                count += frequency // 3 + 1

        return count     