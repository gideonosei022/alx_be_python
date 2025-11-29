
def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats INSIDE the function
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Cannot divide by zero."

        return numerator / denominator

    except ValueError:
        return "Invalid input. Please enter numeric values."


m = safe_divide(10, 2)
print(m)  # Expected output: 5.0

