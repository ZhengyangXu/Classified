"""
Description
___________
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure.
k is given when we create the data structure.

Example
________
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]

Approach
___________
Obvisouly, this is very similar to the previous problem.
Only thing different is when we return top k element, we donot want to
destruct the maintained heap. So we sort the heap and return (not in place)

Complexity
__________
Time - add => Lg(k)
     - topK (Klg(K))
Space - O(K)
"""
