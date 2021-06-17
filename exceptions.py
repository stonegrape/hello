# how to deal with these exceptions
# if someting goes wrong,we want to handle the error nicely, display a nicely error message to
# the user telling them what was wrong instead of having program entirely crash.

# a messy error and a trace-back; catch report
import sys  # module in python called sys
try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:  # if a zero division error happens
    print("Error: Cannot divide by 0")  # then print a error
    sys.exit(1)  # then exit the program
print(f"{x} / {y} = {result}")
