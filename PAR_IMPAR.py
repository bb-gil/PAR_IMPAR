# ejercicio N°4 poder diferenciar si un numero es par o impar

# input

print("-----------------------------------------------------")
X = int(input("digite el valor de X: "))


# processing

r = X % 2
if r == 0:
    rta = "PAR"
    print("el numero es par")

else:
    rta = "IMPAR"
    print("el numero es impar")

print("-----------------------------------------------------")
# output

print("-----------------------------------------------------")
print("el numero" + str(X) + "es" + rta)
print("-----------------------------------------------------")
   

