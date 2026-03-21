'''
INTEGER p,q,r
SET p:= 0 , q:=2 , r:=9
r := 7+p
q:= q+r
FOR EACH r FROM 4 TO 7
                p := (p+p)&q
                IF((p+q)<(r-q)||8<q)
                        p := (p+2)+q
                        JUMP OUT OF THE LOOP
                END IF
END FOR
PRINT p+q '''
p, q, r = 0, 2, 9
r = 7 + p
q = q + r

for r in range(4, 8):
   p = (p + p) & q
   if (p + q) < (r - q) or 8 < q:
       p = (p + 2) + q
       break

print(p + q)
