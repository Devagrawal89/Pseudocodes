'''
FUNCTION simInt(p:INTEGER,r:REAL,t:REAL)RETURN REAL
          DECLARE SI: REAL 
          SI := (p*r*t)/100
          RETURN SI
END FUNCTION

PRINT CALL simInt(12000,8.9,1.2)'''
def simInt(p, r, t):

    si = (p * r * t) / 100
    return si

print(simInt(12000, 8.9, 1.2))
