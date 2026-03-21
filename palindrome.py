'''DECLARE num : INTEGER
DECLARE a : INTEGER
DECLARE b : INTEGER
DECLARE n : INTEGER
SET b := 0
READ num
n := num
WHILE num>0
      a := num MOD 10
      b := b*10+q
      num := num/10
END WHILE
IF
PRINT b == n THEN
             PRINT "Palindrome"
ELSE
             PRINT "Not Palindome"
END IF'''
num = int(input())
n = num
b = 0

while num > 0:
   a = num % 10
   b = b * 10 + a
   num = num // 10
if b == n:
   print("Palindrome")
else:
   print("Not Palindome")
