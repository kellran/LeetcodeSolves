'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        returnList = []
        count = 0
        while(True):
            if len(strs) == 0:
                break

            if len(strs) == 1:
                returnList.append([strs[0]])
                break
            
            
            addList = []
            addList.append(strs[0])
            for i in range(1, len(strs)):

                firstElemSorted = ''.join(sorted(strs[0]))
                checkElemSorted = ''.join(sorted(strs[i]))

                if firstElemSorted == checkElemSorted:
                    addList.append(strs[i])
            returnList.append(addList)
            
            for i in addList:
                if i in strs:
                    strs.remove(i)


        print(returnList)
        return returnList

x = Solution
x.groupAnagrams(x, ["eat","tea","tan","ate","nat","bat"])