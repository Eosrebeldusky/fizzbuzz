a= int(input("Inrese un numero"))
b= int(input("Inrese un numero"))



for i in range (a,b):
    if i%3 == 0 and i%5 == 0:
        print ("FizzBuzz")
    elif i%5 == 0:
        print ("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)


