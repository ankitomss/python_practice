import sys
def makeSuperUgly(primes, n):
    ls=[1]
    k=len(primes)
    p=[0]*k

    count=1
    while count<=n:
        _min=sys.maxint
        for i in range(k):
            if _min > primes[i]*ls[p[i]]:
                _min=primes[i]*ls[p[i]]

        for i in range(k):
            if _min == primes[i]*ls[p[i]]:
                p[i]+=1

        ls+=[_min]
        count+=1

    return ls

primes=[2,7,13,19]
n=12

print makeSuperUgly(primes,n)



