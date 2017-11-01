#M6TI- Kilometer converter
#October 24th, 2017
#Alyssa Freshley
#CTI 110-0002



CONVERSION_FACTOR = 0.6214

def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #display the distance converted to miles
    show_miles(kilometers)

def show_miles(km):
    #calculate miles.
    miles = km* CONVERSION_FACTOR

    #display the miles.
    print(km, 'kilometers equals', miles, 'miles.')
main()
