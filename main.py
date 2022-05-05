def fizzBuzzChoose(x, startPoint, endPoint, Fizz, Buzz):
  for i in range(startPoint, endPoint):
    if x % 5  == 0 and x % 3 == 0:
      return(Fizz, Buzz)
  
    elif x % 3 == 0:
      return(Fizz)
    
    elif x % 5 == 0:
      return(Buzz)
  
    else:
      return(x)

    print(n)

fizzBuzzChoose(n, 1, 50, "Fizz", "Buzz")
