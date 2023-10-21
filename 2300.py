class Solution:
    
    def successfulPairs(self, spells, potions, success: int) :
        import math
        potions.sort()
        pairs = []

        for spell in spells:
            min_potion = math.ceil(success/spell)
            l, r, success_potions = 0, len(potions)-1, 0

            while l <= r:
                mid = (l+r) // 2
                if potions[mid] >= min_potion:
                    success_potions += (r-mid+1)
                    r = mid - 1
                else:
                    l = mid + 1

            pairs.append(success_potions)

        return pairs

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

a = Solution()
a.successfulPairs(spells,potions,success)