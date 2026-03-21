'''DECLARE cn : INTEGER
DECLARE cd : INTEGER
DECLARE pm : INTEGER
DECLARE dbms : INTEGER
DECLARE ml : INTEGER
READ cn,cd,pm,dbms,ml
DECLARE per := REAL
per := cn+cd+pm+dbms+ml / 5
IF per>=90 THEN
        PRINT "A+"
ELSEIF per>=80 THEN
        PRINT "A"
ELSEIF per>=70 THEN
        PRINT "B+"
ELSEIF per>=60 THEN
        PRINT "B"
ELSEIF per>=50 THEN
        PRINT "C"
ELSEIF per>=40 THEN
        PRINT "D"
ELSE
        PRINT "F"
END IF'''
cn = int(input("Enter 1:"))
cd = int(input("Enter 2:"))
pm = int(input("Enter 3:"))
dbms = int(input("Enter 4:"))
ml = int(input("Enter 5:"))

per = (cn + cd + pm + dbms + ml) / 5

if per >= 90:
   print("A+")
elif per >= 80:
   print("A")
elif per >= 70:
   print("B+")
elif per >= 60:
   print("B")
elif per >= 50:
   print("C")
elif per >= 40:
   print("D")
else:
   print("F")