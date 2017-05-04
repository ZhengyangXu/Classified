"""
Description
_____________
Given a string that contains only digits 0-9 and a target value, return all possibilities
to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""


class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def isLeadingZeros(num):
            return num.startswith('00') or int(num) and num.startswith('0')

        def solve(num, target, mulExpr='', mulVal=1):
            ans = []
            # remove leading zeros
            if isLeadingZeros(num):
                pass
            elif int(num) * mulVal == target:
                ans += num + mulExpr,
            for x in range(len(num) - 1):
                lnum, rnum = num[:x + 1], num[x + 1:]
                # remove leading zeros
                if isLeadingZeros(rnum):
                    continue
                right, rightVal = rnum + mulExpr, int(rnum) * mulVal
                #op = '+'
                for left in solve(lnum, target - rightVal):
                    ans += left + '+' + right,
                #op = '-'
                for left in solve(lnum, target + rightVal):
                    ans += left + '-' + right,
                #op = '*'
                for left in solve(lnum, target, '*' + right, rightVal):
                    ans += left,
            return ans
        if not num:
            return []
        return solve(num, target)
