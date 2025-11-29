
def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats INSIDE the function
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return ZeroDivisionError

        return numerator / denominator

    except ValueError:
        return "Invalid input. Please enter numeric values."


# Inputs remain as raw strings
numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

result = safe_divide(numerator, denominator)

print(result)
