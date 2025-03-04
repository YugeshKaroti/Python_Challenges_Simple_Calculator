print("Welcome to the Mathematical Expression Validator and Calculator!")
from modules import validator, calculator
from datetime import datetime
import logging

logging.basicConfig(level = logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

express = input("Enter a mathematical expression (or 'exit' to quit): ")

if express == "exit":
    logging.info("Exiting program.")
    print("Goodbye!")

elif validator.is_valid_expression(express):
    logging.info(f"Valid expression: {express}")
    
    result = calculator.calculate(express)
    
    if result == None:
        pass
        
    else:

        print(f"The result is: {calculator.calculate(express)}")

        logging.info(f"Result of '{express}' is {calculator.calculate(express)}")
        
else:
    print("Invalid expression !")