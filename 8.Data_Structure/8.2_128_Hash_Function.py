"""
Description
___________
In data structure Hash, hash function is used
to convert a string(or any other type) into an integer
smaller than hash size and bigger or equal to zero. The objective of designing
a hash function is to "hash" the key as unreasonable as possible.
A good hash function can avoid collision as less as possible.
A widely used hash function algorithm is using a magic number 33
 consider any string as a 33 based big integer like follow:
hashcode("abcd")
= (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE
= (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
= 3595978 % HASH_SIZE
here HASH_SIZE is the capacity of the hash table (you can assume a hash table
is like an array with index 0 ~ HASH_SIZE-1).
Given a string as a key and the size of hash table
return the hash value of this key.f

Clarification
_____________
For this problem, you are not necessary to design
your own hash algorithm or consider any collision issue
 you just need to implement the algorithm as described.

Example
_________
For key="abcd" and size=100, return 78

Approach
_________
The naive solution will overflow
We do this
for x in key:
    ans = (ans * 33 + ord(x))
    ans %= HASH_SIZE

How does it work? Take 'ab' as an Example
0: a%s
1: ((a%s)*33 + b)%s
   = [((a%s)*33)%s + b%s]%s
   (a+b)%s = (a%s + b%s)%s
   (a*b)%s = (a%s * b%s)%s
   = [(a%s%s * 33%s) + b%s]%s
   a%s%s = a%s
   = (a%s * 33%s + b%s)%s
   = (33*a + b)%s
 And that's what we want. That's why the algorith works by taking a mod
 every time we accumulate the result
 +
 current = 33*current + nums[current_index]

 Compleixty
 ___________
 Time - O(N)
 Space - O(1)
"""
 

class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """

    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x))
            ans %= HASH_SIZE
        return ans
