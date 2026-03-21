'''INTEGER a,b
SET a := 2,b:=50
WHILE(b>0)
    a=b MOD 2+a
    IF(a MOD 3 IS EQUAL TO 0)
                  PRINT (a)
    ELSE
                  PRINT (b-1)
    END IF
    b := b/5
    a := a+1
END WHILE'''
a = 2
b = 50

while b > 0:
   a = (b % 2) + a
   if a % 3 == 0:
       print(a)
   else:
       print(b - 1)

   b = b // 5
   a = a + 1

