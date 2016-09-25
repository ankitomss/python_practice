def calculate():
    v1=v2=v3=v4=v5=0.2
    count=50

    a,b=0.6,0.6
    while count:
        v1,v2,v3,v4,v5=a*(v2/3)+b, a*(v1/2)+b, a*(v2/3+v4)+b, a*(v5)+b, a*(v1/2+v2/3+v3)+b
        print v1, v2, v3, v4, v5
        count-=1


calculate()