start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

even_squares = []
odd_squares = []


for i in range(start, end + 1):
    square = i * i  
    
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("Even Squares:", even_squares)
print("Odd Squares:", odd_squares)