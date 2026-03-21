'''DECLARE num : INTEGER
DECLARE a : INTEGER
DECLARE b : INTEGER
DECLARE Found : BOOLEAN
SET Found := FALSE
WHILE num>0
      a := num MOD 10
      IF a==d THEN
              Found := TRUE
              BREAK
      END  IF
      num := num /10
END WHILE
IF Found == TRUE THEN
                 PRINT "PRESENT"
ELSE
                 PRINT "NOT"
END IF'''
num = int(input("Enter number: "))
d = int(input("Enter digit to find: "))
found = False

while num > 0:
   a = num % 10
   if a == d:
       found = True
       break
   num = num // 10

if found:
   print("PRESENT")
else:
   print("NOT")
