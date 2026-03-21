'''DECLARE Uid,pass: STRING
READ Uid,pass
READ pass
IF Uid=="TIT" AND pass == "TIT" THEN
                 PRINT "Welcome"
ELSE
      PRINT "Invalid Uid"
ENDIF'''
Uid = input()
pass_val = input()

if Uid == "TIT" and pass_val == "TIT":
   print("Welcome")
else:
   print("Invalid Uid")
