def fizzbuzz(start, stop):

    fact1 = 3
    fact2 = 5

    for i in range(start, stop):
        if i % (fact1*fact2) == 0:
            print(f"FizzBuzz")
        if i % fact1 == 0:
            print(f"Fizz")
        if i % fact2 == 0:
            print(f"Buzz")
        else:
            print(i)

fizzbuzz(1,100)