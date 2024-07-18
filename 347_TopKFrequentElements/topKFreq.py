'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numsDict = {}
        returnList = []

        for num in nums:

            if num not in numsDict:
                numsDict[num] = 0
            
            numsDict[num] += 1
        frequency = dict(sorted(numsDict.items(), key=lambda x: x[1], reverse=True))

        keysList = list(frequency.keys())
        for i in range(0, k):
            returnList.append(int(keysList[i]))

        return returnList


x = Solution
print(x.topKFrequent(x, [4,1,-1,2,-1,2,3], 2))