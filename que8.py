'''INTEGER x,y,z
SET x := 10,y :=16, z:=3
IF(x>y)
       x := 2*y
ELSE
       y := x/2
END IF
IF(z>y)
       z := 2*y
ELSE
       y := Z/2
END IF
PRINT x+y+z'''
x, y, z = 10, 16, 3
if x > y:
   x = 2 * y
else:
   y = x // 2

if z > y:
   z = 2 * y
else:
   y = z // 2

print(x + y + z)

