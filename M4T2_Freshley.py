#CTI 110
#M4T2- Python Exercise
#Freshley A
#10/02/2017


#variables


#Ask the user for a string

enterTag= input("What is the string?")



#If it's one of the tags, print "What tag is it" & give example of use



if enterTag == "p":
    print("<p>text</p>")
    print("<p> is the paragraph tag")
 


elif enterTag== "h1": 
    print("<h1>text</h1>")
    print("<h1> is the Header tag")
elif enterTag== "b":
    print("<b>text</b>")
    print("<b> is the bold tag")
elif enterTag== "div":
    print("<div>text</div>")
    print("<div> is the divide tag")
else:
    print("Tag not found")


#Else print "Tag not found"


