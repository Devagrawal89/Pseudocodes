
'''PROCEDURE Artri(b:INTEGER,h:INTEGER)
          DECLARE area:INTEGER
          area :0.5*b*h
          PRINT area
END PROCEDURE

CALL simInt(3,5)'''

def artri(b, h):
    
    area = 0.5 * b * h
    print(area)

artri(3, 5) 
