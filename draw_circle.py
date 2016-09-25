from __future__ import print_function
import math
def draw_circle():
    r = 64
    for i in range(2*r):
        for j in range(2*r):
            dis = math.sqrt(float((i-r)*(i-r) + (j-r)*(j-r)))
            if dis > r-0.5 and dis < r+0.5:
                print ("**", end="")
            else:
                print (" ", end="")
        print ("\n")


draw_circle()