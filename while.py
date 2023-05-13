total = 0
amount = 0
#these variables are necessary to calculate the average at the end




number = int(input("Please enter a number: "))
#asks user input and creates integer 'number'

#creates a while loop below which keeps asking user for number until -1 is entered and 'breaks' the loop
while number > 0:
    total += number #this, in essence, adds the total of inputs together and keeps adding to create the total for average calculation below
    amount += 1 #this adds the total of inputs provided by user for the average calulation
    number = int(input("Please enter a number (or enter -1 to end): "))
    if number == -1:
        break

average = total / amount
#the average is calculated by dividing the total of all the inputs by the amount of inputs made by user

print(average)
#prints the above calculation at the end of the program


#note - used integers and not floats but 'average' produces a float if necessary so happy with the outcome.






