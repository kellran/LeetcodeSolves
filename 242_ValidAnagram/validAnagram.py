'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        s_Sorted = ''.join(sorted(s))
        t_Sorted = ''.join(sorted(t))

        for i in range(0, len(s)):
            if s_Sorted[i] != t_Sorted[i]:
                return False
        
        return True
                
        

x = Solution
x.isAnagram(x, "anagram", "nagaram")
