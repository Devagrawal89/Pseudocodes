'''FUNCTION Cube(x:INTEGER)RETURN REAL
          DECLARE C:INTEGER
          C:= C*C*C
          RETURN C
END FUNCTION

PRINT CALL Cube(3)
'''
def cube(x):
    c = x * x * x
    return c

print(cube(3))
