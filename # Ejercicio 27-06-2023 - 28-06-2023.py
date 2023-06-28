# Ejercicio 27-06-2023 - 28-06-2023
import numpy as np
vLista=([[1,2,3,4,5,6,7,8,9,10],
         [11,12,13,14,15,16,17,18,19,20],
         [21,22,23,24,25,26,27,28,29,30],
         [31,32,33,34,35,36,37,38,39,40],
         [41,42,43,44,45,46,47,48,49,50]])

vMatriz=np.array(vLista)

def reservado(a):
   if a in vMatriz:
      print("\nASIENTO RESERVADO")
      for f in range(5):
         for c in range(10):
            if vMatriz[f][c]==a:
               vMatriz[f][c]=0
               print(f"\n{vMatriz}\n")
   else:
      print("\n[ASIENTO NO DISPONIBLE]\n")

def disponibles():
   for f in range(5):
    vLista=[]
    for c in range(10):
       if vMatriz[f][c]>0:
          vLista.append(vMatriz[f][c])
    print(vLista)
         

flag=True
while flag==True:
  print("[-MENÚ PRINCIPAL-]")
  print("===================================")
  print("[1] Comprar entradas\n[2] Mostrar ubicaciones disponibles\n[3] Ver listado de asistentes\n[4] Mostrar total de ventas\n[5] Salir")
  print("===================================")
  try:
    vOp=int(input("Digite una opción:\n> "))
    if vOp==1:
        vCantEntradas=int(input("Ingrese cantidad de entradas: "))
        if (vCantEntradas<0 and vCantEntradas>3):
           print("ERR: Cantidad solicitada fuera de rango.")
           continue
        elif (vCantEntradas>0 and vCantEntradas<3):
           for n in vCantEntradas:
            vNumAsiento=int(input("Ingrese número de asiento: "))
            reservado(vNumAsiento)
            continue
        else:
           print("ERR: Cantidad inválida.\n")
           continue

    elif vOp==2:
       print("\nASIENTOS DISPONIBLES:")
       disponibles()
       print("")

    elif vOp==3:
        print("\nListado aquí\n")

    elif vOp==4:
        print("\nTotal de ventas aquí\n")

    elif vOp==5:
        print("\nFinalizando...\n")
        break

    else:
        print("\nERR: Opción no se encuentra en el menú.\n")
        
  except:
    print("\nERR: Carácter inválido.\n")