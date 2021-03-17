number = int(input("Enter a number: "))

pattern = ""
for i in range(1, number + 1):
    print(pattern + str(i))
    pattern += str(i)
