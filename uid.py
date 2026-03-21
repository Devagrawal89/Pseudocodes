'''DECLARE Uid: STRING
DECLARE pass: STRING
READ Uid
READ pass
IF Uid=="TIT" THEN
      IF pass == "TIT" THEN**
                 PRINT "Welcome"
      ELSE**
                PRINT "Invalid Passward"
      ENDIF**
ELSE
      PRINT "Invalid Uid"
ENDIF'''
Uid = input()
pass_val = input()

if Uid == "TIT":
   if pass_val == "TIT":
       print("Welcome")
   else:
       print("Invalid Passward")
else:
   print("Invalid Uid")
