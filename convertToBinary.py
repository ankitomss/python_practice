class solution():
    __m=0
    def __mIprivate(self):
        print "yes I am private"

    def _checkme(self):
        print "what am I"

def convertToBinary(x):
    bin=""
    no=0
    fac=1
    while x:
        bit=str(x&1)
        bin=bit+bin
        no=int(bit)*fac+no
        fac*=2
        x=x>>1

    print no
    return bin

print convertToBinary(8)

obj=solution()
#obj.__mIprivate()
obj._checkme()
#print obj.__m
