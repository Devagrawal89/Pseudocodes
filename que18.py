'''INTEGER a,b,c,d
SET b:=10,c:=11
a:= b-c
FOR EACH c FROM 2 TO a LOOP
           b:= b+c+10
           b:= b/2
NEXT c
c:= a+b+c
PRINT a b c'''
b, c = 10, 11
a = b - c
for c_loop in range(2, a + 1):
   b = b + c_loop + 10
   b = b // 2
c = a + b + c
print(a, b, c)
