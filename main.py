def prime_number_checker(number):
    prime_number = True
    for i in range(2, number):
        if number % i == 0:
            prime_number = False
    if prime_number:
        print("This is a prime number")
    else:
        print("This is not a prime number")


numbers = int(input("Please enter a number:"))
prime_number_checker(numbers)
