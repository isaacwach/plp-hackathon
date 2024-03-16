// PROGRAM 1

void main() {
  // Declare and initialize all the variables
  String name = "Isaac";
  int age = 23;
  String school = "PLP academy";
  String hobby = "Reading and coding";

  // Print the user information
  print("Your name is $name, you are $age years old, you school at $school, and you enjoy $hobby.");
}


// PROGRAM 2

void opetations() {
  double number1 = 12.5;
  double number2 = 5;

  //Perform addition operation
  double sum = sum_of_numbers(number1, number2);
  print(sum);

  //Perform modulus operation
  double remainder = remainder_of_numbes(number1, number2);
  print("Remainder: $remainder");
}

// Function to add the two numbers
double sum_of_numbers(double number1, double number2) {
  return number1 + number2;
}

// Function to get the remainder
double remainder_of_numbes(double number1, double number2) {
  return number1 % number2;
}