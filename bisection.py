def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)
    iterations = 0

    # The loop continues as long as the search window is wider than our tolerance
    while (high - low) > tolerance and iterations < max_iterations:
        mid = (low + high) / 2
        square_mid = mid**2

        if square_mid < square_target:
            low = mid
        else:
            high = mid
        
        iterations += 1

    # After the loop, mid is our final refined guess
    root = (low + high) / 2
    
    # Check if we actually met the condition or just ran out of iterations
    if abs(root**2 - square_target) > tolerance:
        print(f"Failed to converge within {max_iterations} iterations")
        return None

    print(f"The square root of {square_target} is approximately {root}")
    return root

result = square_root_bisection(0.001, 1e-7, 50)
print(result)
#0.03162267660168379 and 
#0.031622876601683794
#0.03162384033203125     