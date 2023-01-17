for number in range(1, 101):
    isdivisibleby3 = number % 3 == 0
    isdivisibleby5 = number % 5 == 0
  
    if isdivisibleby3  and isdivisibleby5:
        print("Fizzbuzz")
    elif isdivisibleby3:
        print("Fizz")
    elif isdivisibleby5:
        print("buzz")
    else:
        print(number)
    