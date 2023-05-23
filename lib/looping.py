#!/usr/bin/env python3
def happy_new_year():
    count = 10
    while (count > 0):
        print(f"{count}")
        count -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    squared_list = ([int ** 2 for int in int_list])
    return squared_list

def fizzbuzz():
    num = 1
    while (num <= 100):
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
            num += 1
        elif (num % 3 == 0):
            print("Fizz")
            num += 1
        elif (num % 5 == 0):
            print("Buzz")
            num += 1
        else:
            print(num)
            num += 1
