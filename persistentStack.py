class persistentStack(object):
    def __init__(self, ls, x):
        self.st=ls
        self.end=x

    def getst(self):
        return self.st

    def getend(self):
        return self.end

    def setend(self, x):
        self.end=x

    def getlength(self):
        return self.end

    def _print(self):
        print self.st[:self.end]

st1=persistentStack([], 0)

def push(no, st1):
    return persistentStack(st1.getst()[:st1.getend()] +[no], st1.getlength()+1)

def pop(st1):
    return persistentStack(st1.getst(), st1.getend()-1)

def peek(st1):
    return st1.getst()[st1.getend()-1]

def size(st1):
    return st1.getlength()

def empty():
    return persistentStack([],0)


st4=push(1,st1)
st5=push(2,st4)
st2=push(3, st1)
st6=pop(st5)
st6._print()
print st6.getend()
print peek(st6)
print size(st6)
st6=empty()






# def pop1(st):
#     return len(st)-1

st=[1,2]



# print push1(3, st, pop1(st))
#
# def pop(st):
#     n=len(st)
#     return st[:n-1]
#
# print pop(st)
# print st
#
# def peek(st):
#     return st[-1]
# print peek(st)
# print st
#
# def size(st):
#     return len(st)
#
# def empty():
#     return []
#
# st1=empty()
# st2=push(1,st1)
# st3=push(2,st2)
# st4=pop(st3)
#
# print st1, st2, st3, st4
