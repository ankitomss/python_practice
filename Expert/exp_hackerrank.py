# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
In Mathematics, exponentiation has higher operator precedence than multiplication. This means that any exponentiation
in the expression must be evaluated first before before any multiplication. For the purposes of this challenge,
exponentiation is left-associative, which is different than you would normally evaluate it. This means that  is
 evaluated as  and not as .

In Python, the exponentiation operator is denoted by a double asterisk (**). For example,  is expressed as a**k.
To express multiplication, we use a single asterisk operator, *. For example, we express  as a*b.

An expression, , consisting of decimal digits and asterisks is valid if and only if it forms a valid mathematical
expression when each double-asterisk (i.e., **) is replaced with a math exponentiation sign. For example, 2**4*5**3
 is a valid expression translating to , while *2**3, 2***3, 4*5**, and 4**2* are invalid as they do not translate to
 valid mathematical expressions.

Given  expressions consisting of decimal digits and asterisks, parse each expression and determine its validity.
If an expression is valid, print its evaluated value modulo  on a new line; if it's invalid, print Syntax Error instead.
"""
import math, numpy
def calculate(s, st, exp):
    if exp > 2 or (not st and exp) or (not s and exp):
        print "Syntax Error"
        return

    if not s:
        num = long(1)
        for i in range(len(st)):
            num *= st[i]
        print num % (10**9 + 7)
        return

    print s
    if s[0] == "*":
        calculate(s[1:], st, exp+1)
    elif s[0].isdigit():
        num, i = "", 0
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        print "num is ", num, exp
        if exp == 2:
            st.append(numpy.power(st.pop(), int(num)) % (10**9+7))
        else:
            st.append(long(num))
        calculate(s[i:], st, 0)
    else:
        print "Syntax Error"



print math.pow(10**9+7, 10) % (10**9+7)
##calculate("1234234**1324123*2", [], 0)

def cal_power(n1, n2):
    result, n1 = 1, n1
    for i in range(n2/10):
        result *= (math.pow(n1, 10) % (10**9+7))

    result *= (math.pow(n1, n2%10) % (10**9+7))
    return result % (10**9+7)

print cal_power(123, 12)
print math.pow(123, 12) % (10**9+7)


