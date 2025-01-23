# a number that is only divided by 1 and by itself

number = int(input("Enter the number: "))

for i in range (2,number):
    if number % i == 0:
        print("Not prime number: ")
        break
    else:
        print("prime number: ")
