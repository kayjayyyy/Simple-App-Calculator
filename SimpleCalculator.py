# Templanza, Kristine Joy F.
# BSCPE 1-4
# Asignnment no. 5 - Simple App Calculator

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 40)
print("")
print("\033[45m ♥ Welcome to our calculator program! ♥ \033[0m".center(85))

# Ask the name of the user 
name = input("\n\033[033mGood day! What is your name? \033[0m")
print("\n\033[3;33mI hope you are doing well,", name + "!\033[0m")
print("")

print("\033[36m Let's get started! \033[0m".center(88, "~"))
print("\n")

# Print the math operation choices
print("\033[36ma. Multiplication\033[0m".center(85))
print("\033[36mb. Division\033[0m".center(85))
print("\033[36mc. Addition\033[0m".center(85))
print("\033[36md. Subtraction\033[0m".center(85))

# Ask the user for math operation they want to perform
math = input("\n\033[33;3mPlease choose a math operation you want to use (a/b/c/d): \033[0m")

# Ask the user for the integer
first_number = float(input("\n\033[33;3mEnter your first number: \033[0m"))
second_number = float(input("\n\033[33;3mEnter your second number: \033[0m"))

a = "*"
b = "/"
c = "+"
d = "-"

# Generate the program to perform the calculation
try:
    total = ""
    if math == "a":
        total = first_number * second_number
        
    elif math == "b":
        total = first_number / second_number
        
    elif math == "c":
        total = first_number + second_number
        
    elif math == "d":
        total = first_number - second_number
    else:
        print("Error input character")
    
    # Print the calculated total
    print("\n\033[32mThe calculated total is: ", total, "\033[0m")
    
    # Ask the user if they want to calculate again
    while True:
        input_again = input("\nDo you want to calculate again (yes or no)? ")
        # If yes, ask again for their choice of math operation
        if input_again == "yes":
            
            print("\n")
            print("\033[35m Let's get started! \033[0m".center(88, "~"))
            print("\n")
            
            # Print the math operation choices
            print("\033[36ma. Multiplication\033[0m".center(85))
            print("\033[36mb. Division\033[0m".center(85))
            print("\033[36mc. Addition\033[0m".center(85))
            print("\033[36md. Subtraction\033[0m".center(85))

            # Ask the user for math operation they want to perform
            math = input("\n\033[33;3mPlease choose a math operation you want to use (a/b/c/d): \033[0m")

            # Ask the user for the integer
            first_number = float(input("\n\033[33;3mEnter your first number: \033[0m"))
            second_number = float(input("\n\033[33;3mEnter your second number: \033[0m"))
            
            # Generate the program to perform the calculation
            total = ""
            if math == "a":
                total = first_number * second_number
            
            elif math == "b":
                total = first_number / second_number
            
            elif math == "c":
                total = first_number + second_number
            
            elif math == "d":
                total = first_number - second_number
            else:
                print("Error input character")
            
            # Print the calculated total       
            print("\n\033[32mThe calculated total is: ", total, "\033[0m")
            break
        
        # If no, break and stop the program
        else:
            break

# Use except value error to handle error encounter
except ValueError: 
    print("INVALID: Error input characters!")
    
# Outro and border line
print("\n")
print("\033[3mThank you for supporting our program!".center(85))
print("")
print("\033[35m※ \033[0m" * 40)
print("")