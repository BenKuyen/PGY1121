flag=True
vEntradaNiño=5500
vContNiño=0
vEntradaJoven=7000
vContJoven=0
vEntradaAdulto=9000
vContAdulto=0
vAcum=0
while flag==True:
    print("[-CINE MORO-]\n¡Buenos días, y bienvenidos a Cine Moro!\n")
    print("=======================")
    print("1-. Niño ($ 5500 CLP)")
    print("2-. Joven ($ 7000 CLP)")
    print("3-. Adulto ($ 9000 CLP)")
    print("4-. Generar Boleta")
    print("5-. Salir")
    print("=======================")

    try:
        vOp=int(input("\n-----------------------\nSeleccione una opción:\n> "))
        if (vOp>0 and vOp<4):
            vCantidad=int(input("¿Cuántas entradas desea tener?\n> "))
            if vOp==1:
                vContNiño+=vCantidad
                vAcum+=vCantidad*vEntradaNiño
            elif vOp==2:
                vContJoven+=vCantidad
                vAcum+=vCantidad*vEntradaJoven
            elif vOp==3:
                vContAdulto+=vCantidad
                vAcum+=vCantidad*vContAdulto

        elif vOp==4:
            print("[-BOLETA DE PAGO-]")
            print("Tipo de Entrada         Cantidad         SubTotal")
            print("Entrada Niño           ",vContNiño,"               $",vContNiño*vEntradaNiño,"CLP")
            print("Entrada Joven          ",vContJoven,"               $",vContJoven*vEntradaJoven,"CLP")
            print("Entrada Niño           ",vContAdulto,"               $",vContAdulto*vEntradaAdulto,"CLP")
            print(f"Total a pagar: $ {vAcum} CLP")
            print("\n¡Gracias por su compra, disfrute de la función!\n")
            
            vContNiño=0
            vContJoven=0
            vContAdulto=0
            vAcum=0
        
        elif vOp==5:
            print("Cerrando programa...\nGracias por venir, ¡disfrute la función!\n")
            flag=False
        else:
            print("Opción no válida. Intente de nuevo.")


    except:
        print("Ingreso no válido. Intente de nuevo.")

print("Finalizando...")