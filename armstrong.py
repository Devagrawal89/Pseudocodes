'''DECLARE num : INTEGER
DECLARE a : INTEGER
DECLARE b : INTEGER
DECLARE n : INTEGER
SET b := 0
READ num
WHILE num>0
      a := num MOD 10
      b := b+a*a*a
      num := num/10
END WHILE
IF
PRINT b == n THEN
             PRINT "Armstrong Number"
ELSE
             PRINT "Not Armstrong Number"
END IF'''
num = int(input())
n = num
b = 0
while num > 0:
   a = num % 10
   b = b + (a * a * a)
   num = num // 10

if b == n:
   print("Armstrong Number")
else:
   print("Not Armstrong Number")