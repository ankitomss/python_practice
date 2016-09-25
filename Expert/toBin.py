def toBin(num):
    ret = ""
    neg = (num < 0)
    bit = {0:"01", 1:"10"}
    num = -num if neg else num
    i = 0
    while i < 32:
        id = num%2
        ret += bit[neg][id]
        num /= 2
        i += 1
    return ret[::-1]

import sys
num = 0
num = sys.maxint - abs(num) + 1 if num < 0 else num
# print str(bin(num))[-32:].lstrip("0b")
print hex(int(bin(num), 2))[-8:]
print str(hex(int(bin(num),2)))[-8:].lstrip("0x")