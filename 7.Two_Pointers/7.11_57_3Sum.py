"""
Description
__________
Given an array S of n integers
are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

example
__________
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)

Approach
___________
Based on 2Sum, have an extra for loop
then set left  = i + 1
do 2Sum while

Code is self-explantory
Complexity

Be careful about the skipping duplicates part
__________
Time - O(N^2)
Space - O(1)



We can also have a general findKSum approach, we will discuss in detail in 4sum
"""


class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) == 0:
            return []
        numbers.sort()
        result = []

        for i in xrange(len(numbers) - 3 + 1):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                v = numbers[left] + numbers[right]
                if v == 0 - numbers[i]:
                    while left < right and numbers[left + 1] == numbers[left]:
                        left += 1
                    while left < right and numbers[right - 1] == numbers[right]:
                        right -= 1
                    result.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                elif v < 0 - numbers[i]:
                    left += 1
                else:
                    right -= 1
        return result


class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        result, branch = [], []
        numbers.sort()
        self.ksum(numbers, 0, 3, 0, branch, result)
        return result

    def ksum(self, numbers, start, k, target, branch, result):
        # print k
        if k == 0:
            return
        if k == 1:
            for i in numbers:
                if i == target:
                    branch.append(i)
                    result.append(branch[:])
                    branch.pop()
        if k == 2:

            # print "here", branch
            i, j = start, len(numbers) - 1
            while i < j:
                # print "in while"
                v = numbers[i] + numbers[j]
                if v == target:
                    # print i,j,numbers
                    while i < j and numbers[i] == numbers[i + 1]:
                        i += 1
                    while i < j and numbers[j] == numbers[j - 1]:
                        j -= 1
                    branch.append(numbers[i])
                    branch.append(numbers[j])
                    # print branch, numbers[i], numbers[j],i,j
                    result.append(branch[:])
                    branch.pop()
                    branch.pop()

                    i += 1
                    j -= 1
                elif v < target:
                    i += 1
                else:
                    j -= 1
            return
        for i in xrange(start, len(numbers) - k + 1):
            if i != start and numbers[i] == numbers[i - 1]:
                continue
            branch.append(numbers[i])
            self.ksum(numbers, i + 1, k - 1, target - numbers[i], branch, result)
            branch.pop()
