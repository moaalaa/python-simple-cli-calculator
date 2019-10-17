import re

# Application Intro
print("""
   _____ _      _____    _____      _            _       _             
  / ____| |    |_   _|  / ____|    | |          | |     | |            
 | |    | |      | |   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    | |      | |   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |____| |____ _| |_  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____|______|_____|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|                                                                       
  __________________________________________________________________
  Simply Calculator using CLI
                                    
""")

print("Press Ctrl+C for exit")

print("---------------------------------------")

# Previous Results by default 0
previous = 0

# Determine Whether to continue calculate or not
run = True

# Calculate 
def calculate():

    # Get global variables "run" and "previous" for modification.
    # Use "global" Keyword only if need to modify a global variables.
    # You can access global variables without "global" key word.    
    global run, previous

    # Set Equation To Empty value
    equation = None

    # If "previous" Is 0 Then Prompet User
    if previous == 0:
        equation = input("Enter Your Equation: ")

    # If "previous" Is Not 0 then prompet the string version of "previous"
    else:
        equation = input(str(previous))

    # Clean "equation" from any alphabetical and signs not related to "Math"
    equation = re.sub('[A-Za-z,:()"\'" "]', '', equation)

    # If "previous" is equal 0 then "eval" the "equation"
    if previous == 0:
        previous = eval(equation)

    # If "previous" not equal 0 then contact the "equation" with string version of "previous" finally eval it
    else:
        previous = eval(str(previous) + equation)

# Run Application
while run:
    calculate()
