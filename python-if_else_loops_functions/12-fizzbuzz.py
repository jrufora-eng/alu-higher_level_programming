#!/usr/bin/python3
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        out = "FizzBuzz"
    elif i % 3 == 0:
        out = "Fizz"
    elif i % 5 == 0:
        out = "Buzz"
    else:
        out = str(i)
    
    if i == 100:
        print(out, end="")
    else:
        print(out, end=" ")
print()
