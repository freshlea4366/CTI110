#CTI 110
#M3T1- Area of Rectangles
#Alyssa Freshley
#09/13


#calc area of 2 rectangles
firstWidth = int(input("Width of first?"))
firstLength = int(input("Length of first?"))

secondWidth = int(input("Width of second?"))
secondLength = int(input("Length of second?"))

#Calculate areas- width * length
#Area= width* length
firstArea = firstWidth*firstLength
secondArea = secondWidth*secondLength

#now, compare the two areas
if firstArea> secondArea:
    print('first is bigger')

else:
    if firstArea< secondArea:
            print('Second is bigger')

    else:
        #equal
        print('They are equal size')

    print('done')
    
