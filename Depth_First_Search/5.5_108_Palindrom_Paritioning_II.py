"""
Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Have you met this question in a real interview? Yes
Example
Given s = "aab",

Return 1 since the palindrome partitioning ["aa", "b"] could be produced using 1 cut.

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        f = []
        p = [[False for x in range(n)] for x in range(n)]
        #the worst case is cutting by each char
        for i in range(n+1):
            f.append(n - 1 - i) # the last one, f[n]=-1
        for i in reversed(range(n)):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]




shuizhongdeyu
__________
        凡是求最优解的，一般都是走DP的路线。这一题也不例外。首先求dp函数，

定义函数
D[i,n] = 区间[i,n]之间最小的cut数，n为字符串长度

 a   b   a   b   b   b   a   b   b   a   b   a
                     i                                  n
如果现在求[i,n]之间的最优解？应该是多少？简单看一看，至少有下面一个解


 a   b   a   b   b   b   a   b   b   a   b   a
                     i                   j   j+1     n

此时  D[i,n] = min(D[i, j] + D[j+1,n])  i<=j <n。这是个二维的函数，实际写代码时维护比较麻烦。所以要转换成一维DP。如果每次，从i往右扫描，每找到一个回文就算一次DP的话，就可以转换为
D[i] = 区间[i,n]之间最小的cut数，n为字符串长度， 则,

D[i] = min(1+D[j+1] )    i<=j <n

有个转移函数之后，一个问题出现了，就是如何判断[i,j]是否是回文？每次都从i到j比较一遍？太浪费了，这里也是一个DP问题。
定义函数
P[i][j] = true if [i,j]为回文

那么
P[i][j] = str[i] == str[j] && P[i+1][j-1];


1:       int minCut(string s) {
2:            int len = s.size();
3:            int D[len+1];
4:            bool P[len][len];
5:            //the worst case is cutting by each char
6:            for(int i = 0; i <= len; i++)
7:            D[i] = len-i;
8:            for(int i = 0; i < len; i++)
9:            for(int j = 0; j < len; j++)
10:            P[i][j] = false;
11:            for(int i = len-1; i >= 0; i--){
12:                 for(int j = i; j < len; j++){
13:                      if(s[i] == s[j] && (j-i<2 || P[i+1][j-1])){
14:                           P[i][j] = true;
15:                           D[i] = min(D[i],D[j+1]+1);
16:                      }
17:                 }
18:            }
19:            return D[0]-1;
20:       }  
"""
