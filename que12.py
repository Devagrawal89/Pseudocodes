'''INTEGER x:=9, y:=2, z:=6
INTEGER a
a := a&y|z
PRINT a
	x, y, z = 9, 2, 6
a = x & y | z
print(a)


Code38:

INTEGER a,b,c,d,e
SET a:= 50, b:=3 , c:=3, e:=0
WHILE(c>0)
          d := a MOD b
          e := e+d+a
          c := c-1
END WHILE
PRINT e'''
a, b, c, e = 50, 3, 3, 0
while c > 0:
   d = a % b
   e = e + d + a
   c = c - 1
print(e)

