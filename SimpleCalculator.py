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
print("\033[36ma. Multiplication\033[0m".center(85))
print("\033[36mb. Division\033[0m".center(85))
print("\033[36mc. Addition\033[0m".center(85))
print("\033[36md. Subtraction\033[0m".center(85))

math = input("\n\033[33;3mPlease choose a math operation you want to use (a/b/c/d): \033[0m")

first_number = float(input("\n\033[33;3mEnter your first number: \033[0m"))
second_number = float(input("\n\033[33;3mEnter your second number: \033[0m"))

a = "*"
b = "/"
c = "+"
d = "-"

try:
    total = ""
    if math == "a":
        total = first_number * second_number
        
    elif math == "b":
        total = first_number / second_number
        
    elif math == "c":
        total = first_number + second_number
except ValueError: 
    print("INVALID: Error input characters!")
    