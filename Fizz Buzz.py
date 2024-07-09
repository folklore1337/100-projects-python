def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
        elif i% 3== 0:
            result.append("Fizz")
        elif i% 5== 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
    
print(fizzbuzz(15))
print(fizzbuzz(30))
print(fizzbuzz(50))
print(fizzbuzz(100))