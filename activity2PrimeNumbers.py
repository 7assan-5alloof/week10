number = int(input("Enter a number: "))

if number == 1 or number == 0:
    print(f"The number {number} is neither primary nor composite")
    exit(0)
for i in range(2, number):
    if number == i:
        continue
    elif number % i == 0:
        print("The number is composite")
        exit(0)
print("The number is prime")
