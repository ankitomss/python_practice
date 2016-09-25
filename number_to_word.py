class test(object):
    def __init__(self):
        self.val = None

digits = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight","Nine", "Ten","Eleven", "Twelve", "Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def int2english(num):
    if num >= 1000000000:
        return int2english(num / 1000000000) + " Billion" + int2english(num % 1000000000)

    if num >= 1000000:
        return int2english(num / 1000000) + " Million" + int2english(num % 1000000)

    if num >= 1000:
        return int2english(num / 1000) + " Thousand" + int2english(num % 1000)

    if num >= 100:
        return int2english(num / 100) + " Hundred" + int2english(num % 100)

    if num >= 20:
        return " " + tens[num / 10 - 2] + int2english(num % 10)

    if num > 0:
        return " " + digits[num - 1]

    return ""


def numberToWords(num):
    if num == 0:
        return "Zero"

    ans = int2english(num)
    ans = ans.strip()
    return ans

print numberToWords(1000100)
