#!/usr/bin/env python3

# Author ID: 120352224

def operate(number1, number2, operator):
   
    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    elif operator == 'divide':
        
        if number2 == 0:
            return 'Error: Cannot divide by zero'
        result = number1 / number2
    else:
        return 'Error: function operator can be "add", "subtract", "multiply", or "divide"'
    
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))         # Output: 15
    print(operate(10, 5, 'subtract'))    # Output: 5
    print(operate(10, 5, 'multiply'))    # Output: 50
    print(operate(10, 5, 'divide'))      # Output: 2.0
    print(operate(10, 0, 'divide'))      # Output: Error: Cannot divide by zero
    print(operate(10, 5, 'unknown'))     # Output: Error: function operator can be "add", "subtract", "multiply", or "divide"
