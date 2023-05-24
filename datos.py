print("\nDATOS PERSONALES")
print("-----------------\n")
vNom=input("Ingrese su nombre:\n> ")
while True:
 try:
    vEdad=int(input("Ingrese su edad:\n> "))
    break
 except:
    print("\nERR: Valor no corresponde.")

print("-----------------\n")
print(f"Su nombre es {vNom}.")
print(f"Su edad es de {vEdad} años.\n")

print("Finalizando proceso...")