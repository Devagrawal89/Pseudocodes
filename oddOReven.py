'''
DECLARE x: INTEGER
READ x
IF x MOD 2 == 0 THEN
         PRINT "EVEN"
ELSE
       PRINT "ODD"
END IF
'''
x = int(input())
if x % 2 == 0:
    print("EVEN")
else:
    print("ODD")
