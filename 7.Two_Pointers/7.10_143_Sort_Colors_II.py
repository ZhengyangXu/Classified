"""
Description
__________
Given an array of n objects with k different colors (numbered from 1 to k)
sort them so that objects of the same color are adjacent
with the colors in the order 1, 2, ... k.

Example
_____________
Given colors=[3, 2, 2, 1, 4], k=4
 your code should sort colors in-place to [1, 2, 2, 3, 4].


Approach/Compleixty
_________________
Deep Two Pointers
++++++++++++++++
Understand how Two pointers work
Then have an extra while loop to maintain Min, Max = 1, k

After the end of inner while loop (of two pointers sort)

Update  i = left
        Min += 1
        Max -=1

Time - O(kn)
Space - O(1)

Counting Sort
+++++++++++++++
Same as last problem


In place Counting Sort
+++++++++++++++
This is a very clever algorithm. We are essentially trying to use the colors array
itself to construct c and then loop from behind to update value to the correct
final position

we use position n-1 at colors to store the frequncy of value n element

0. for i in xrange(n):
1.    deal with i, stay at i until it's <= 0. This translates to a while loop
      While colors[i] > 0:
          v = colors[i]
          (a) when colors[v-1] > 0.
              it means at position v-1, there is already an element
              we need to deal with later.
              So we swap the value to i, next while loop will then deal with it
              and set colors[v-1] to -1 indicates value v now has frequncy 1

              swap(colors,i,v-1)
              colors[v-1] = -1


          (b) when colors[v-1] <= 0
              It means at position v-1 (which indicates freq of v), it has nothing
              to deal with and ready to increment the count of freq
              So we set colors[v-1] = colors[v-1] - 1(increment freq count)
              and we set colors[i] = 0 (since no more value to deal with)

              colors[v-1] -= 1
              colors[i] = 0
2. Now colors[0:k] have the correct freq count (0 stands for 1, k-1 stands for k)
   Essentially we know have c in the counting sort
   other unsed parts [k:] of colors will be 0

   Since we lost our original colors array
   We do
   Initialize index = len(colors) - 1
   We start from back to avoid overwrite
   For i in xrange(k-1, -1, -1)  (it's k -1 because how we stored freq in colors)
        cnt = -colors[i] -- Grab the count of freq for element i + 1
        (a) when cnt is 0, skip (continue)
        (b) when cnt > 0
            while cnt > 0:
                colors[index] = i + 1
                cnt -= 1
                index -= 1

  Two pass
  Time - O(N)
  Space - O(1)





"""

#  Deep Two Pointers
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        Min, Max = 1, k
        left, right = 0, len(colors) - 1
        i = 0
        while Min < Max:
            while i <= right:
                if colors[i] == Min:
                    self.swap(colors, i, left)
                    i += 1
                    left += 1
                elif colors[i] == Max:
                    self.swap(colors, i, right)
                    right -= 1
                else:
                    i += 1
            i = left
            Min += 1
            Max -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


# Counting Sort
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        n = len(colors)
        output = [0 for _ in xrange(n)]
        c = [0 for _ in xrange(k + 1)]
        for v in colors:
            c[v] += 1
        for i in xrange(1, k + 1):
            c[i] = c[i] + c[i - 1]
        for i in xrange(n):
            output[c[colors[i]] - 1] = colors[i]
            c[colors[i]] -= 1
        for i in xrange(n):
            colors[i] = output[i]


# in-place Counting Sort
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        n = len(colors)
        for i in xrange(n):
            while colors[i] > 0:
                num = colors[i]
                if colors[num - 1] > 0:
                    colors[i] = colors[num - 1]
                    colors[num - 1] = -1
                elif colors[num - 1] <= 0:
                    colors[i] = 0
                    colors[num - 1] -= 1
        index = len(colors) - 1
        for i in xrange(k - 1, -1, -1):
            cnt = -colors[i]
            if cnt == 0:
                continue
            while cnt > 0:
                colors[index] = i + 1
                cnt -= 1
                index -= 1
