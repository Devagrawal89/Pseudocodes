
'''a = 4 , b = 4 , c = 2
Integer funn(Integer a , Integer b , Integer c)
        Integer c 
        Set c = a+a+b+b
        b = c+c+b+b
        a = b-a 
        return a+b
end function funn()
'''

def funn(a,b,c):
    c = a+a+b+b
    b = c+c+b+b
    a = b-a 
    return a+b
print(funn(7,4,2))
