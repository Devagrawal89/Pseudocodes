'''
PROCEDURE simInt(p:INTEGER,r:REAL,t:REAL)
          DECLARE SI: REAL 
          SI := (p*r*t)/100
          PRINT SI
END PROCEDURE

CALL simInt(1000,2.3,1.2)
'''
def simInt(p, r, t):
    si = (p * r * t) / 100
    print(si)

simInt(1000, 2.3, 1.2)

