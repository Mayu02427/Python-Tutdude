import math
num = float(input("Enter a positive number: "))
if num > 0:
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)         # Natural logarithm (base e)
    sine_result = math.sin(num)        # Sine in radians

    # Step 3: Display results
    print(f"\nResults for the number {num}:")
    print(f"Square Root: {sqrt_result}")
    print(f"Natural Logarithm (ln): {log_result}")
    print(f"Sine (in radians): {sine_result}")
else:
    print("Please enter a number greater than 0 for valid square root and log calculations.")
