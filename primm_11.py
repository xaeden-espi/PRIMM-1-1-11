"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""

def main():
    name: str = input("What is your name? ")
    print("Hello,", name, "!")
  
    num1: int = input("Enter a number: ")
    num2: int = input("Enter another number: ")
    total: int = num1+num2
    
    print(f"{num1} + {num2} = {total}")

if __name__ == "__main__":
  main()
