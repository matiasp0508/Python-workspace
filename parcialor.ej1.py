
def pais_invalido(destino_pais) -> bool:
    return destino_pais not in ["Brasil", "Chile", "Estados Unidos", "España"]

def carga_paquetes_nuevos(paquetes_disponibles:dict) -> None:
    print("Los paises disponibles son: Brasil, Chile, Estados Unidos, España. ")
    destino_pais = ("Ingrese Pais para crear un nuevo paquete: ")
    
    while pais_invalido(destino_pais):
        print(f"el pais seleccionado no existe en el sistema. Por favor ingrese un pais valido: ")
        
    nombre_paquete = ("Ingreseel nombre del nuevo paquete: ")
    
    cantidad_dias = ("Ingrese cantidad de dias: ")
    
    valor_paquete = ("Ingrese el nuevo valor: ")
    
    paquetes_disponibles[destino_pais][nombre_paquete] = (cantidad_dias, valor_paquete)   
    
    

def cargar_ventas(ventas:dict, paquetes_disponibles:dict) -> None:
    
    DNI = input("Ingrese Nro de DNI para registrar compra: ")

    nombre = input("Ingrese solo primer Nombre: ")
    apellido = input("Ingrese Apellido: ")
    
    print("Los paises disponibles son:")
    print("Brasil")
    print("Chile")
    print("Estados Unidos")
    print("España")
    destino_pais = (input("Ingrese el destino donde desea viajar: "))
    while pais_invalido(destino_pais):
        print(f"El pais seleccionado no existe. Por favor ingrese un pais valido: ")
    
    print(f"Los paquetes disponibles son: {paquetes_disponibles(nombre_paquete, destino_pais)}")
    nombre_paquete = ("Ingrese el paquete deseado")
    
    cantidad_pasajeros = input("Ingrese cantidad de pasajeros contando tambien el comprador: ")
    valor_a_pagar = cantidad_pasajeros * destino_pais[nombre_paquete][1]
    ventas[DNI] = (nombre, apellido, destino_pais, cantidad_pasajeros, valor_a_pagar)
    
    print(f" El valor a pagar es ${valor_a_pagar}")
        
    


def imprimir_opciones() -> None:
    print()
    print(“-”*10)
    print(“Menu de opciones:”)
    print(“a. Cargar ventas.”)
    print(“b. Cargar paquetes turisticos.”)
    print(“c. Listar todas las reservas por destino.”)
    print(“d. Imprimir paquete mas vendido.”)
    print(“e. Imprimir pasajero que mas reservas realizo.”)
    print(“f. Listar todas las ventas cuyos montos totales sea mayor al promedio.”)
    print(“g. Salir.”)



def opcion_invalida(opt:str) -> bool:
    return opt not in ["a", "b", "c", "d", "e", "f", "g"]


def sleccion_opcion() -> str:
    imprimir_opciones()
    opt = input("Ingrese una opcion: ")

    while opcion_invalida(opt):
        opt = input(f"La opcion [{opt}] es invalida. Por favor ingrese una opcion valida.")

    return opt    




def main() -> None:
    print("Bienvenido al software de Te llevo a donde quieras S.R.L.")
    
    ventas = {} #{ dni[nombre, apellido, destino, cantidad_de_pasajeros, valor_a_pagar]}
    paquetes_disponibles = {} #{destino_pais{nombre_paquete[cantidad_dias, valor], paquete2[valor]}
    opt = seleccion_opcion()
    
    while opt != "g":
        if opt == "a":
            pass
        elif opt == "b":    
            pass
        elif opt == "c":    
            pass
        elif opt == "d":    
            pass
        elif opt == "e":    
            pass
        elif opt == "f":    
            pass
        opt = seleccion_opcion()    
    return    

main()    
