# PLD - Practice

## Week 0: Hello World, Conditions, Loops, Functions

### Hello World 

#### 1. Create a Personalized Greeting

- **Task**: Ask the user for their name and store it in a variable. Then, print a greeting message that includes their name.
- **Example**: Input: "Alice", Output: "Hello, Alice! Welcome to Python."

#### 2. Extract Initials from a Full Name
- **Task**: Take a full name as input and extract the initials using string slicing. Then, print the initials in uppercase.
- **Example**: Input: "John Doe", Output: "Your initials are J.D."

#### 3. Reverse a String
- **Task**: Ask the user to input a word or sentence. Use string slicing to reverse the input and print the reversed string.
- **Example**: Input: "Python", Output: "nohtyP"

#### 4. Create a Simple Username Generator
- **Task**: Ask the user for their first name and last name. Generate a username by combining the first three letters of the first name with the last three letters of the last name. Ensure all letters are lowercase.
- **Example**: Input: "John Smith", Output: "johith"

#### 5. Hide a Part of a Phone Number
- **Task**: Ask the user for their phone number. Replace the middle part of the number with asterisks for privacy and print the result.
- **Example**: Input: "123-456-7890", Output: "123-***-7890"

### Conditions, Loops, Functions

#### 1: Simple Input and Output
- Write a function `greet_user()` that asks the user for their name and prints a greeting: "Hello, [name]!".

#### 2: Even or Odd Checker
- Write a function `check_even_odd()` that asks the user to input a number and prints whether the number is even or odd.

#### 3: Summing Numbers in a Range
- Write a function `sum_numbers()` that asks the user for two numbers, `a` and `b`, and prints the sum of all numbers between them (inclusive).

#### 4: Counting Vowels in a String
- Write a function `count_vowels()` that takes a string as input from the user and counts the number of vowels (`a, e, i, o, u`) in it. Return and print the count.

#### 5: Simple Password Validator
- Write a function `check_password()` that takes a password input from the user and checks whether it contains at least 8 characters and includes both letters and digits. If valid, print "Password is strong", otherwise "Weak password".

#### 6: Multiplication Table Generator
- Write a function `print_table()` that takes an integer input from the user and prints the multiplication table (up to 10) for that number.

#### Sum of Digits
- Write a function `sum_of_digits()` that takes a positive integer input and prints the sum of its digits. For example, if the input is 345, it prints 12 (3 + 4 + 5).

#### Reverse a String
- Write a function `reverse_string()` that takes a string as input and prints its reverse. For example, if the input is "hello", it prints "olleh".

#### Prime Number Checker
- Write a function `check_prime()` that takes an integer input and checks whether the number is prime or not. Print "Prime" if true, otherwise print "Not Prime".

#### Number Guessing Game
- Write a function `guess_number_game()` that generates a random number between 1 and 100 (you can hardcode the number) and asks the user to guess it. Provide hints if the guess is too high or too low, and end the game when the correct number is guessed.

#### Final Integration Task (Bonus)
- Combine these functions into a small interactive program where the user is prompted to choose which task to perform (via menu selection).