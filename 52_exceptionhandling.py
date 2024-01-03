# Errors
# - Compile Time
# - Logical
# - Run Time

x = 14

try:
    y = int(input("Enter a number"))
    print("Resource Open")
    print(x / y)

except ZeroDivisionError as e:
    print("You are dividing by zero", e)

except ValueError as e:
    print("Invalid Input", e)

except Exception as e:
    print("Something went wrong...")

finally:
    print("Resource Closed")
