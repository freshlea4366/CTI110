#CTI 110
#M3HW1: Age classifier
#Freshleya
#09/20

def main():
    age = int(input("What is the age?"))
    
    if age<= 1:
        print("They are an infant")
    elif age >1 or age < 13:
        print("They are a child")
    elif age >= 13 and age <20:
        print("they are a teenager")
    elif age >= 20:
        print("They are an adult")

main()
