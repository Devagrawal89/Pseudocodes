'''a=3,b=8.c=7
Integer function(Integer 1, Integer b, Integer c)
    If((a^8)<8)
        c=a+c
        c=a+c
    END if
return a+b+c'''
def func(a, b, c):
    if (a^8) < 8:
        c = a + c
        c = a + c
    return a + b + c

a = 3
b = 8
c = 7

print(func(a, b, c))