# FUNCTIONS AND FIBONACCI SEQUENCE

# Create a function that takes n as a parameter
def fibonacci_sequence(n):
    sequence = [0, 1]

    #Loop through from 2 to n and keep increamenting the subsequent values
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