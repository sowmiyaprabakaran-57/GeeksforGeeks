#User function Template for python3
n=int(input())
def fizzbuzz(n):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)
fizzbuzz(n)