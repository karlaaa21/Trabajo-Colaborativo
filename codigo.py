num1= int(input("Ingrese el primer numero "))
num2= int(input("Ingrese el segundo numero "))
num3= int(input("Ingrese el tercer numero "))

contador_par= 0
contador_impar= 0 

if num1 % 2 == 0 :
    contador_par += 1
else :
    contador_impar +=1

if num2 % 2 == 0 :
    contador_par += 1
else :
    contador_impar += 1

if num3 % 2 == 0 :
    contador_par += 1
else:
    contador_impar += 1
print(f"numeros pares ingresados : {contador_par}")
print(f"numeros impares ingresados : {contador_impar}")

suma_total= num1 + num2 + num3

if suma_total > 100 : 
    print("La suma total es mayor a 100")
