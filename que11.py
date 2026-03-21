'''INTEGER x,y,z
SET x := 10,  y := 16, z:= 3
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
PRINT x+y+z'''
x, y, z = 10, 16, 3
if x > y:
   x = y
else:
   y = x

if z > y:
   x = y
else:
   y = z
print(x + y + z)