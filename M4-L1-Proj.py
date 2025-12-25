def square_odd_even(start, end):
    squares = [i**2 for i in range(start, end + 1)]

    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)


square_odd_even(1, 10)
