'''a = 5 , b = 5, c = 5 
Integer funn(Integer a , Integer b , Integer c)
        if ((c&a)<a & (a*b)<b)
                    c = (a*2)+b
        end if 
        return a+b+c
end funn'''
def funn(a,b,c):
    if ((c&a)<a & (a*b)<b):
        c = (a*2)+b
    return a+b+c
print(funn(5,5,5))
