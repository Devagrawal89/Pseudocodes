'''INTEGER x,y,z
SET x := 8,  y := 6, z:=4
IF(x>y)
       x := y
ELSE
       y := x
END IF
IF(z>y)
       x := y
ELSE
       y := z
END IF
PRINT x+y+z '''
x, y, z = 8, 6, 4
if x > y:
   x = y
else:
   y = x

if z > y:
   x = y
else:
   y = z

print(x + y + z)
