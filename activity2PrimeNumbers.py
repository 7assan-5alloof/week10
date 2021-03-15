number = int(input("Enter a number: "))

for i in range(2, 11):
    if number == i:
        continue
    if number % i == 0:
        print("The number is composite")
        exit(0)
print("The number is prime")