

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact


def e():
    limite = 4
    n = 0
    suma = 0
    while n < limite:
        suma += 1/factorial(n)
        n = n + 1
     


    print(f"El valor de e es -> {suma}")

 
e()
