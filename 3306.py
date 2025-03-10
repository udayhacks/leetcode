""" 3306. Count of Substrings Containing Every Vowel and K Consonants II
Solved
Medium
Topics
Companies
Hint
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5 """


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        cnt_vowel = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        left, start, cnt_diff_vowel, ans = 0, 0, 0, 0
        for ch in word:
            if ch in cnt_vowel:
                cnt_vowel[ch] += 1
                if cnt_vowel[ch] == 1:
                    cnt_diff_vowel += 1
            else:
                k -= 1
                
            while k < 0 or cnt_diff_vowel == 5 and cnt_vowel.get(word[left], 0) > 1:
                ch_left = word[left]
                left += 1
                if ch_left in cnt_vowel:
                    cnt_vowel[ch_left] -= 1
                    if cnt_vowel[ch_left] == 0:
                        cnt_diff_vowel -= 1
                else:
                    k += 1  
                    start = left
                       
            if cnt_diff_vowel == 5 and k == 0:
                ans += left - start + 1
        return ans
    
    
a = Solution()
print(a.countOfSubstrings("ieaouqqieaouqq", 1))