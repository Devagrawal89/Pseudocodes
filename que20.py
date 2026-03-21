'''//Called with a=9,b=7 and c=20

INTEGER funn(INTEGER a ,INTEGER b ,INTEGER c)
        IF ((a+c)<(b-a))
                 c = 4+b
                 b = (c+c)+b
        ELSE
                 c = (a+3)^a
                 c = (10&8)+b
        END IF
        RETURN a+b+c
END funn
	//Called with a=9,b=7 and c=20
'''

def funn(a,b,c):
    if ((a+c)<(b-a)):
        c = 4+b 
        b = (c+c)+b
    else:
        c = (a+3)^a
        c = (10&8)+b
    return a+b+c
print(funn(9,7,20))
