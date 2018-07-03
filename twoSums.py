"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, 
or some other object which supports iteration. The __next__() method of the iterator 
returned by enumerate() returns a tuple containing a count 
(from start which defaults to 0) and the values obtained from iterating over iterable.
"""

def twoSum(nums, target):
    lookup = { }
    for cnt, num in enumerate(nums):
        if target - num in lookup:
            return lookup[target-num], cnt
        lookup[num] = cnt

print(twoSum([2,7,11,15],9))
    
