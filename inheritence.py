class parent(object):
    def call(self):
        print "this is parent"

class child(parent):
    def callchild(self):
        print "this is child"

x=child()
x.call()
x.callchild()
p=parent()
p.call()