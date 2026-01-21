def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return float(square_target)

    low = 0.0
    high = max(1.0, square_target)

    for _ in range(max_iterations):
        mid = (low + high) / 2
        mid_squared = mid * mid

        if abs(mid - square_target**0.5) < tolerance:   # if we could compute it...
            # but since we can't, we use squared difference scaled
            pass

        # Better: check relative size of interval
        if (high - low) < tolerance:
            root = (low + high) / 2
            print(f"The square root of {square_target} is approximately {root}")
            return root

        if mid_squared < square_target:
            low = mid
        else:
            high = mid

    root = (low + high) / 2
    print(f"Failed to converge within {max_iterations} iterations")
    return None
result = square_root_bisection(0.001, 1e-7, 50)
print(result)
print(square_root_bisection(225, 1e-7, 10)) #should return None
# #0.03162267660168379 and 
# #0.031622876601683794
# #0.03162384033203125     

# def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
#     if square_target < 0:
#         raise ValueError("Square root of negative number is not defined in real numbers")

#     if square_target == 0 or square_target == 1:
#         print(f"The square root of {square_target} is {square_target}")
#         return square_target

#     low = 0
#     high = max(1, square_target)
#     iterations = 0

#     # The loop continues as long as the search window is wider than our tolerance
#     while (high - low) > tolerance and iterations < max_iterations:
#         mid = (low + high) / 2
#         square_mid = mid**2

#         if square_mid < square_target:
#             low = mid
#         else:
#             high = mid
        
#         iterations += 1

#     # After the loop, mid is our final refined guess
#     root = (low + high) / 2
    
#     # Check if we actually met the condition or just ran out of iterations
#     if abs(root**2 - square_target) > tolerance:
#         print(f"Failed to converge within {max_iterations} iterations")
#         return None

#     print(f"The square root of {square_target} is approximately {root}")
#     return root

# result = square_root_bisection(0.001, 1e-7, 50)
# print(result)
# #0.03162267660168379 and 
# #0.031622876601683794
# #0.03162384033203125     