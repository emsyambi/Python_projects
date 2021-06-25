# Fibonacci series
# The sum of two elements defines the next

a, b = 0, 1

while a < 100000:
    print(a, end=" ")
    # The keyword argument end can be used to avoid the newline after the output
    a, b = b, a+b

