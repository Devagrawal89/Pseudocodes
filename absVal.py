'''FUNCTION absVal(a:REAL):REAL
         IF a>0 THEN 
                RETURN a
         ELSE 
                RETURN -a
         END IF
END FUNCTION
PRINT absVal(1)
PRINT absVal(-8)'''
def absVal(a):
    if a>0:
        return a 
    else:
        return -a
print(absVal(1))
print(absVal(-8))


'''
PROCEDURE absVal(a:REAL) 
         IF a>0 THEN
                PRINT a
         ELSE
                PRINT -a
         END IF
END PROCEDURE 
CALL(5)
CALL(-5)'''
def absVal(a):
    if a>0:
        print (a) 
    else:
        print (-a)
absVal(5)
absVal(-5)
