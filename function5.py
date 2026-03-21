'''
FUNCTION AriTri(b:REAL,h:REAL):REAL
         DECLARE area :REAL
         area := 0.5*b*h
         RETURN area
END FUNCTION 
PRINT AriTri(2,5)'''
def AriTri(b,h):
    area = 0.5*b*h
    return area
print(AriTri(20,20))


