'''INTEGER p,q,r,s
SET p:=4,q:=3,r:=1
s:=(p AND q)OR(r+1)
PRINT s'''
p, q, r = 4, 3, 1
s = (p & q) | (r + 1)
print(s)
