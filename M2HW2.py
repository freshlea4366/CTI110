#CTI110
#M2HW2- Tip, Tax, Total
#Alyssa Freshley
#09/13


#foodCost= 60.0
foodCost= float(input("What is the foodCost ? "))
#print('The foodCost is $', foodCost)
print('The foodCost is $', format(foodCost,' .2f'))

tipAmount= 0.18 * foodCost
#print ('The tip is $', tipAmount)
print('The tip is $', format(tipAmount,'.2f'))


tax= 0.07 *foodCost
#print('The tax is $', tax)
print ('The tax is $', format (tax,' .2f'))



total= foodCost + tipAmount + tax
print('The total is $', format (total,' .2f'))

      
