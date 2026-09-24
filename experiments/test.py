import math

def karatsuba_multiply(x: int, y: int) -> int:
    """
    Simulates CPython's recursive Karatsuba multiplication.
    Uses base-10 and a low cutoff for easy tracing.
    """
    # Fallback to standard multiplication if numbers are small (Simulates CPython's CUTOFF)
    if x < 1000 or y < 1000:
        return x * y

    # Calculate the size of the numbers
    string_x, string_y = str(x), str(y)
    n = max(len(string_x), len(string_y))
    
    # M is the split point (half the number of digits)
    m = n // 2

    # Split the numbers into high and low chunks
    # x = a * 10^m + b
    # y = c * 10^m + d
    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    print(f"[Split] n={n}, m={m} -> X split into ({a}, {b}), Y split into ({c}, {d})")

    # Step 1: Recursive call for high digits (P1 = a * c)
    p1 = karatsuba_multiply(a, c)

    # Step 2: Recursive call for low digits (P2 = b * d)
    p2 = karatsuba_multiply(b, d)

    # Step 3: Recursive call for cross-sum combinations (P3 = (a + b) * (c + d))
    p3 = karatsuba_multiply(a + b, c + d)

    # Step 4: Karatsuba trick to extract the middle term (ad + bc) without multiplying them
    middle_term = p3 - p1 - p2

    # Step 5: Shift components into their correct base positions and combine
    # (Equivalent to bit-shifting left by 2M and M inside CPython)
    result = (p1 * (10 ** (2 * m))) + (middle_term * (10 ** m)) + p2
    
    return result

# --- Execution ---
if __name__ == "__main__":
    # Two large numbers that trigger the split logic
    num1 = 12345678
    num2 = 87654321

    print(f"Multiplying {num1} × {num2}\n" + "-"*50)
    
    karatsuba_result = karatsuba_multiply(num1, num2)
    actual_result = num1 * num2

    print("-"*50)
    print(f"Karatsuba Result : {karatsuba_result}")
    print(f"Standard Result  : {actual_result}")
    print(f"Verification     : {'Success! Match confirmed.' if karatsuba_result == actual_result else 'Failed.'}")
