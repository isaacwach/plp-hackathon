# FUNCTIONS AND FIBONACCI SEQUENCE

# Create a function that takes n as a parameter
def fibonacci_sequence(n):
    sequence = [0, 1]

    #Loop through from 2 to n and keep increamenting the last two values in the sequence, and append them to the sequence
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence

# Ask the user to input the value of n
n = int(input("Enter the value of n: "))

# Generate the Fibonacci sequence
fibonacci = fibonacci_sequence(n)

# Print the generated Fibonacci sequence
print(f"Fibonacci sequence up to term {n}: {fibonacci}")


# PYTHON CONDITIONAL STATEMENTS PROBLEM SOLUTION
def voting_condition():
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
voting_condition()

# Using less lines of code
def voting():
    age = int(input("Enter your age: "))
    print("You are eligible to vote" if age >= 18 else "You are not eligible to vote")

voting()