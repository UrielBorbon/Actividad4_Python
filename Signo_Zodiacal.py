#Programa que muestre que signo Zodiacal perteneces. (IF-ELSE)
dia = int(input("Digite el dia de Nacimiento: \n"))
mes = int(input("Digite el mes de Nacimiento (Num): \n"))

if (dia >= 21 and dia <= 31 and mes == 3) or (dia >= 1 and dia <=19 and mes == 4):
    print("Tu signo es Aries")
elif (dia >= 20 and dia <= 30 and mes == 4) or (dia >= 1 and dia <=20 and mes == 5):
    print("Tu signo es Tauro")
elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <=20 and mes == 6):
    print("Tu signo es Geminis")  
elif (dia >= 21 and dia <= 30 and mes == 6) or (dia >= 1 and dia <=22 and mes == 7):
    print("Tu signo es Cancer")    
elif (dia >= 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <=22 and mes == 8):
    print("Tu signo es Leo")
elif (dia >= 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <=22 and mes == 9):
    print("Tu signo es Virgo")
elif (dia >= 23 and dia <= 30 and mes == 9) or (dia >= 1 and dia <=22 and mes == 10):
    print("Tu signo es Libra")
elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <=21 and mes == 11):
    print("Tu signo es Escorpion")
elif (dia >= 22 and dia <= 30 and mes == 11) or (dia >= 1 and dia <=21 and mes == 12):
    print("Tu signo es Sagitario")
elif (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <=19 and mes == 1):
    print("Tu signo es Capricornio")
elif (dia >= 20 and dia <= 31 and mes == 1) or (dia >= 1 and dia <=18 and mes == 2):
    print("Tu signo es Acuario")
elif (dia >= 19 and dia <= 28 and mes == 2) or (dia >= 1 and dia <=20 and mes == 3):
    print("Tu signo es Piscis")
else:
    print("Fecha Invalida xv")
    