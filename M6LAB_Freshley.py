#M6LAB-
#CTI 110
#November 1, 2017
#Alyssa Freshley




def main():
    name = input("What is your name?")
    greet(name)
    age= int(input("What is your age?"))
    print("You are a:", ageCategory(age))

def greet(name):
    ''' greet user by name'''
    print("Hello", name)

def ageCategory(age):
    if age <= 1:
       category= 'infant'
    elif age >1 and age < 13:
        category= 'child'
    elif age >=13 and age <20:
        category= 'teenager'
    else:
        category= 'adult'



    return category



main()


    
