class Solution(object):
    def make(self, num, target, prev, curstr, result):
        if prev != 1 and prev*int(num) == target:
            if len(num) == 1 or num[0] != '0':
                curstr += num
                result.append(curstr)

        if not num:
            return

        if int(num) == target and prev==1:
            if len(num) == 1 or num[0] != '0':
                curstr += num
                result.append(curstr)
                return

        for i in range(1, len(num)):
            a, b = int(num[:i]), int(num[i:])

            if num[0] == '0' and len(num[:i]) > 1: continue
            for c in "+-*":
                if c == '+': self.make(num[i:], target-a*prev, 1, curstr+num[:i]+'+', result)
                elif c == '-': self.make(num[i:], a*prev-target, 1, curstr+num[:i]+'-', result)
                elif c == '*':
                    self.make(num[i:], target, prev*a, curstr+num[:i]+'*', result)


    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        curstr, result = "", []
        self.make(num, target, 1, curstr, result)
        return result

print Solution().addOperators('105', 5)