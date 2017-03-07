"""
Description
___________
Given an array S of n integers
are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Approach
__________
We can then have another additional for loop based on 4SUM to achive this
But here we present a general kSum algorithm using DFS

Code is self-explantory, becareful with skipping duplicates

Complexity
_________
Time - O(N^k-1)
Space - O(K)

"""


class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of
              zero.
    """

    def fourSum(self, numbers, target):
        # write your code here
        result = []
        numbers.sort()
        # print numbers

        self.ksum(numbers, 0, 4, target, [], result)
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
