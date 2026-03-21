'''
a = 6,b = 9,c = 2
Integer funn(Integer a , Integer b , Integer c)
        for(each c from 4 to 8)
                 a = (a+11)+b
                 a = (c+3)+b
        end for 
        b = (5+10)+a
        a = (10+8)+a
        for (each c from 2 to 5)
            a = (10+2)+a
            b = (3+4)+a
        end for
        return a+b
End funn	'''
def funn(a,b,c):
    for c in range (4,9):
        a = (a+11)+b
        c = (c+3)+b
    
    b = (5+10)+a
    a = (10+8)+a
    for c in range(2,6):
        a = (10+2)+a
        b = (3+4)+a
    
    return a+b 
print(funn(6,9,2))

