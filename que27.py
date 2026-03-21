'''
a=2,b=6,c=1
Integer funn (Integer a, Integer b, Integer c)
    if ((c^b+a) <(a&c)) 
         b=a^b 
         c=(a+3)+C
    End if

     if ((3^b)+ (c^c)> (11&c))
        b2 (C+12)^a
     End if
return a+b+c'''

def funn(a, b, c):
    if (c^b + a) < (a & c):
        b = a^b
        c = (a + 3) + c
    if (3^b + c^c) > (11 & c):
        b = ((c + 12) ^ a)

    return a + b + c

a = 2
b = 6
c = 1

print(funn(a, b, c))