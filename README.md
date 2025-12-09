Project Overview and Objectives
This project is a Python program designed to evaluate student performance. It accepts a numerical score input and outputs a letter grade along with a personalized, encouraging message. The objective was to practice using control flow statements (if-elif-else), functions, and input validation techniques.
Setup and Installation Instructions
Ensure Python is installed: This script requires Python 3.x.

Download the file: Clone the repository or download grade_calculator.py.

Run the application: Open your terminal or command prompt and run:python grade_calculator.py
Code Structure and Logic Explanation
Function get_grade_and_message(score):

This function encapsulates the grading logic.

It uses an If-Elif-Else chain to check the score against grade boundaries (90, 80, 70, 60).

It returns two values: the letter Grade and a corresponding Message.

Input Validation:

Type Check: A try-except block is used to catch ValueError if the user types text instead of numbers.

Range Check: An if statement ensures the number is strictly between 0 and 100.
screenahot:<img width="1330" height="246" alt="Screenshot 2025-12-09 213446" src="https://github.com/user-attachments/assets/d47f3d15-0e02-4354-80d0-e5a0c07cff80" />
How Technical Requirements Were Met
Use if-elif-else statements: Implemented in the get_grade_and_message function to determine the specific grade tier.

Add input validation: Used try-except for non-numbers and logic checks for the 0-100 range.

Create at least one function: Created the modular function get_grade_and_message() to separate logic from input handling.
TEST CASE REPORT

Test 1: Normal Success (A Grade)
Input: 95
Expected Output: Grade A, "Outstanding work!"
Result: Pass

Test 2: Normal Success (C Grade)
Input: 72.5
Expected Output: Grade C, "Good effort."
Result: Pass

Test 3: Boundary Check (Minimum Pass)
Input: 60
Expected Output: Grade D
Result: Pass

Test 4: Boundary Check (Fail)
Input: 59
Expected Output: Grade F
Result: Pass

Test 5: Invalid Input (Out of Range High)
Input: 105
Expected Output: Error: Please enter a number between 0 and 100.
Result: Pass

Test 6: Invalid Input (Out of Range Low)
Input: -10
Expected Output: Error: Please enter a number between 0 and 100.
Result: Pass

Test 7: Invalid Input (Non-numeric)
Input: eighty
Expected Output: Error: Invalid input. Please enter a numeric value.
Result: Pass

