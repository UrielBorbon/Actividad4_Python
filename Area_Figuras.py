# b = base, h = altura
opc = int(input("Digite la opcion: \n"))

def triangulo():
    area = float((b * h) / 2)
    print("El area del triangulo es: ", area)

def circulo():
    area2 = float((pi * r * r))
    print("El area del circulo es: ", area2)

def cuadrado():
    area3 = float((l * l))
    print("El area del cuadrado es: ", area3)

if opc == 1:
    b=float(input("Digite la base del Triangulo: \n"))
    h=float(input("Digite la altura del Triangulo: \n")) 
    triangulo()
elif opc == 2:
    r=float(input("Digite el radio del Circulo: \n"))
    pi = 3.1416
    circulo()
elif opc == 3:
    l=float(input("Digite el lado del Cuadrado: \n"))
    cuadrado()
else:
    print("Opcion Invalida")

