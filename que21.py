'''
//Called with a=9,b=7 

INTEGER funn(INTEGER a, INTEGER b)
        DECLARE c: INTEGER 
        SET c:= 2 
        b := b MOD c
        a:= a MOD c
        RETURN a+b
END funn()
	//Called with a=9,b=7 
'''
def funn(a,b):
    c = 2 
    b = b%c
    a = a%c 
    return a+b
print(funn(9,7))

