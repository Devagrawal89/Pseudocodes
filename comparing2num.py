'''DECLARE num1 : INTEGER
DECLARE num2 : INTEGER
READ num1,num2
IF num1>num2 THEN
        PRINT "num1 is greater"
ELSE
       PRINT "num2 is greater"
END IF
'''
num1 = int(input())
num2 = int(input())
if num1 > num2:
   print("num1 is greater")
else:
   print("num2 is greater")