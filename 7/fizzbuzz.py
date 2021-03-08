def fizzbuzz(n): # Prints FizzBuzz for range 1 to n
        return "Fizz"*(n%3==0)+"Buzz"*(n%5==0) or n

if __name__ == "__main__":
        for i in range(1,101):
            print(fizzbuzz(i))
