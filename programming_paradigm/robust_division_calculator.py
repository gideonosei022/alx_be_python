  def safe_divide(numerator, denominator):
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: ")) 
    if denominator == 0:
        return None
    return numerator / denominator


try:
    result = safe_divide(numerator, denominator)
    if result is None:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of {numerator} divided by {denominator} is {result}.")
except ValueError:
    print("Invalid input. Please enter numeric values for numerator and denominator.")

