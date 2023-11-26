class Solution:
   
    def groupAnagrams(self, strs):
        from collections import defaultdict
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        print(anagram_map)
        
        return list(anagram_map.values()) 



strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
a = Solution()
a.groupAnagrams(strs)