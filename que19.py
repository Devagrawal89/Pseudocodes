'''DECLARE p : INTEGER
DECLARE q : INTEGER
SET q:=30, p:=10, r:=20
IF(r>(r+p))
     q := 1
ELSE
     p:= p-2
     r:= r-2
END IF
IF(r>(r+p)MOD 11) THEN
          q:= (a^5)
ELSE
          p:= p+2
ENDIF'''
q, p, r = 30, 10, 20
if r > (r + p):
   q = 1
else:
   p = p - 2
   r = r - 2
if r > (r + p) % 11:
   q = pow(p, 5)
else:
   p = p + 2

print(p ,q , r)
