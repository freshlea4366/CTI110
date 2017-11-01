#M5T2= Bug collector
#10/09/17
#Alyssa Freshley
def main():
    total = 0
    for day in range(1,8):
        print("Enter the bugs collected on day", day)
        bugs = int(input())
        total += bugs
        print("You collected a total of", total, 'bugs.')
main()
