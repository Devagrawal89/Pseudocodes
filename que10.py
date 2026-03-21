'''INTEGER p,q,r,sum
READ p,q,r
IF((p NOT EQUALS 0) AND (SUM EQUALS 11) AND (q EQUALS 4) AND (r NOT EQUALS 0))
                    PRINT "Success"
OTHERWISE
                   PRINT "Fail"
END IF'''
	
p = int(input())
q = int(input())
r = int(input())
sum_val = int(input())
if p != 0 and sum_val == 11 and q == 4 and r != 0:
   print("Success")
else:
   print("Fail")