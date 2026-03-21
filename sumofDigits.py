'''DECLARE num : INTEGER
DECLARE a : INTEGER
DECLARE b : INTEGER
SET b := 0
READ num
WHILE num>0
      a := num MOD 10
      b := b+a
      num := num/10
END WHILE
PRINT b'''
num = int(input())
b = 0

while num > 0:
   a = num % 10
   b = b + a
   num = num // 10

print(b)
