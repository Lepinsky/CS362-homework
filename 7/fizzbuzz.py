def fizzbuzz(n): # Prints FizzBuzz for range 1 to n
    for i in range(1,n):
        print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)

if __name__ == "__main__":
    fizzbuzz(100)
