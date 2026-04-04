# Last updated: 04/04/2026, 13:11:23
class Solution:

    def isAcronym(self, words: List[str], s: str) -> bool:

        acronym=''.join(i[0] for i in words)

        return acronym==s
