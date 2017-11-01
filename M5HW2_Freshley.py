#M5HW2- Running Totals
#Freshley, Alyssa
#October 16, 2017
#CTI 110



runningTotal= 0
#loop, adding input to total

repeat= True

def main():
    runningTotal = 0
    keepGoing= True

    
    while keepGoing:
        #keep going until the user types a negative
        print('Enter a number:')
        number = int(input('>'))
        if number < 0:
            keepGoing= False
        else:
            #add the number to the total
            runningTotal = runningTotal + number
    #print the total
    print('Total is:',runningTotal)
main()
