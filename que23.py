'''a = 4 , b = 4 , c = 7 
Integer funn(Integer a , Integer b , Integer c)
        for(each c from 3 to 5)
                   a = (c+c)^b
                   if ((a+c) < (c+a))
                             b = (a+11)+c 
                   else 
                             c = b+b
                             a = 8+b
                             continue 
                   end if 
       end for 
return a+b	'''

def funn(a,b,c):
    for each in (3,6):
        a = (c+c)^b
        if ((a+c) < (c+a)):
            b = (a+11)+c 
        else :
            c = b+b
            a = 8+b
            continue 
    return a+b
print(funn(4,4,7) )     

