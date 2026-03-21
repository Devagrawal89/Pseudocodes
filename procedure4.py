'''PROCEDURE Cube(x:INTEGER)
          DECLARE C:INTEGER
          C:= C*C*C
          PRINT C
END PROCEDURE

CALL Cube(3)
'''
def cube(x):
    c = x * x * x
    print(c)
    
cube(3) 
