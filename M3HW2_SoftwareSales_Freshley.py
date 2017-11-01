#cti 110
#m3hw2- software sales
#freshleya
#09/20

#quantity = price* discount
def main():
    quantity= int(input("What is the quantity?"))
    discount = 0
    price= 99
    if quantity <= 10 and quantity <= 19:
        print("10% discount")
        discount= .1
    if quantity <20 and quantity >= 49:
        print("20% discount")
        discount = .2
    if quantity >= 50 and quantity <= 99:
        print("30% discount")
        discount = .3
    if quantity <= 100:
        print("40% discount")
        discount = .4
    
    totalCost = quantity * price

main()
