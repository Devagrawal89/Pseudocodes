'''INTEGER a,b,c
SET b:= 4 , c:= 5
FOR EACH a FROM 2 TO 4 LOOP
                PRINT c
                b:= b-1
                c:= c+b
NEXT FOR'''
b = 4
c = 5
for a in range(2, 5):
   print(c)
   b = b - 1
   c = c + b