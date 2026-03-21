'''PROCEDURE mxelm(a:INTEGER,b:INTEGER)
          IF x>y THEN 
                 PRINT "Max is x"
          ELSE 
                 PRINT "Max is y"
END PROCEDURE

CALL simInt(1,8)'''

def mxelm(a, b):
    if a > b:
        print(f"Max is {a}")
    else:
        print(f"Max is {b}")

mxelm(1, 8) 
