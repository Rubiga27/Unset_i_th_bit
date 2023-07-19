def update_bit(A, B):
    mask = 1 << B

    if (A & mask) != 0:
        A &= ~mask

    return A

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

updated_A = update_bit(A, B)
print(updated_A)
