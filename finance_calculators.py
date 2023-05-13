import math

print("investment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan\n\nEnter either 'investment' or 'bond' from the menu above to proceed:")
#prints the opening message. \n used to separate lines; \n\n used to insert blank line to make it look better..

while True:
    selection = input("\nEnter choice:\n").lower() 
#creates string for input with blank line above and converts to lower case

    if selection == "investment":
        P = int(input("\nEnter deposit amount:\n"))
        r = int(input("\nEnter interest rate\n"))
        r = (r/100) #converts 'r' in to a percentage by dividing by 100
        t = int(input("\nEnter length in years of planned investment\n"))
        interest = input("\nEnter either 'simple' or 'compound' for selected interest rate\n")
    #the above creates the integer strings as requested in the task and allows the user to input required info


        #both maths formulas below copied from task pdf worksheet
        #basic if/elif statements allow for the correct calucations to be done
        if interest == "simple":
            A = P*(1 + r*t)
        elif interest == "compound":
             A = P * math.pow((1+r),t)
        print("\nTotal return:" , A)
        break #ends loop as no further need for any more code to be executed


    
    elif selection == "bond":
       P = int(input("\nEnter value of house:\n"))
       i = int(input("\nEnter monthly interest rate:\n"))
       i = (i/100/12) #ensures integer i is a percentage by dividing by 100 and that it's monthly by dividing by 12
       n = int(input("\nEnter number of months over which bond to be repaid\n"))

       repayment = (i * P)/(1 - (1 + i)**(-n)) #as above, formula copied from worksheet pdf

       print("\nMonthly repayments:" , repayment)
       break

    else:
        print("Invalid selection. Please try again")
        #loops back if 'bond' or 'investment' are not created via input 










