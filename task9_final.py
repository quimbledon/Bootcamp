
#1) First part of the code creates a text file to store data and the next line creates an empty list to store the inputted equations.
equations_file = "equations.txt"
equations = [] 

# opens file in "append" mode (creating a list of inputted equations) and store file object in variable "f"
with open(equations_file, "a") as f:
    
    while True:
        #2) this section of code allows for input of a number and prevents erroneous non-integer inputs via try/except block
        while True:
            try:
                x = int(input("Please enter your first number:\n"))
                y = int(input("Please enter another number:\n"))
                break
            except ValueError:
                print("Error. Please enter a valid whole number")
        
        #3) inputs operator and loops back until valid input is selected
        #(added .lower to help correct with x if inputted as X)
        while True:
            operator = input("Please enter +, -, x or /:\n").lower()
            if operator in ["+", "-", "x", "/"]:
                break
            else:
                print("Invalid input")
        
        #4) calculate result; #also avoids python 'divide by zero' error by making user reselect operator
        if operator == "+":
            user_number = x + y
        elif operator == "-":
            user_number = x - y
        elif operator == "x":
            user_number = x * y
        elif operator == "/":
            if y == 0:
                print("Cannot divide by zero, try again")
                continue
            else:
                user_number = x / y
        
        #4) this section creates the end equation, prints it and also saves it to the associated txt file
        #**#the \n below seemed vital in making the txt file a list rather than rows of outputs..
        equation = f"{x} {operator} {y} = {user_number}\n"
        equations.append(equation)
        f.write(equation)
        print(equation)
        f.flush() #before I added this line, printing all equations from text file presented a blank result
        #researched flush() method which ensures the data is written to txt file before moving to step 5
        
        #5) this code section allows user to continue to produce equations or to move to printing equations from txt
        while True:
            choice = input("Do you want make further calculations? (y/n)\n").lower()
            if choice in ["y", "n"]:
                break
            else:
                print("Invalid selection. Please enter y or n")
        
        if choice == "n":
            break
    
    #6) below asks the user if they want to read and print equations from equations.txt
    #try/except block used if file name entered incorrectly
    #added prompt for typing equations.txt otherwise the line would seem confusing for a user as equations.txt isn't mentioned to user
    while True:
        choice = input("Do you want to read all equations from file? (y/n)\n").lower()
        if choice == "y":
            while True:
                try:
                    filename = input("Please enter the name of the text file to retrieve the equations (default: equations.txt):\n")
                    if filename == "":
                        filename = equations_file
                    with open(filename, "r") as f:
                        equations_from_file = f.readlines()
                        print("All equations:\n")
                        for equation in equations_from_file:
                            print(equation)
                        break
                except FileNotFoundError:
                    print("File not found. Please enter a valid file name.")
                    continue
            break
        elif choice == "n":
            break
        else:
            print("Invalid selection. Please enter y or n")




#seems to work ok. wasn't too sure about user entering equations.txt; needed prompt as entered above

#tried to break up the code a bit more after my first attempt as it was struggle with my previous attempt to..
#..add the enter file name section.

#sections 1-5 deal with the calculations and saving data to file - this forms the first 'half'
#section 6 I added to access the txt file and forms the end half

