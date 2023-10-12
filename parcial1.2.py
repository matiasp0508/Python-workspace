
def mostrar_plato_mas_solicitado(platos: dict) -> None:   
    pass

def mostrar_el_cliente_mas_pedidos(pedidos_clientes: dict) -> None:
    pass

def mostrar_pedido_mayor_valor(pedidos_clientes: dict, platos: dict) -> None:
    maximo_valor: int = 0
    id_pedido_maximo_valor: str = ""
    primer_id: bool = True
    for cuit_cliente in pedidos_clientes:
        for pedido in pedidos_clientes[cuit_cliente]:
            valor_total_pedido = 0
            for id_plato in pedidos_clientes[cuit_cliente][id_pedido]:
                valor_plato = platos[id_plato]["precio"]
                valor_total_pedido += valor_plato
                if primer_id:
                    maximo_valor = valor_total_pedido
                    id_pedido_maximo_valor = id_pedido
                    primer_id = False
                if valor_total_pedido > maximo_valor:
                    maximo_valor = valor_total_pedido
                    id_pedido_maximo_valor = id_pedido
    print("El peido de mayor valor es: ", id_pedido_maximo_valor)
    print()


def listar_pedidos(pedidos_clientes: dict) -> None:
    cuit_cliente = input("Ingrese el cuit para ver sus pedidos: ")
    for pedido in pedidos_clientes[cuit_cliente]:
        print(pedido)

def pedido_valido(string: str, platos:dict) -> bool:
    split = string.split(",")
    for s in split:
        if not s.isnumeric():
            return False
    if len(split) < 1:
        return False
    for id_plato in platos:
        if id_plato not in platos:
            return False
    return True


def agregar_pedido(platos: dict, pedidos_clientes: dict, contador_id_pedidos: list[int]) -> None:
    for plato in platos:
        print(plato, ": ", platos[plato])
    cuit_cliente = input("Ingrese el cuit del cliente: ")
    platos_pedido = input("Ingrese los datos del pedido separados por coma (ej. 1, 2, 3)")
    if not pedido_valido(platos_pedido):
        while not pedido_valido(platos_pedido):
            platos_pedido = input("Ingrese los datos del pedido separados por coma (ej. 1, 2, 3)")
    platos_pedido: list[str] = platos_pedido.split (",")
    contador_id_pedidos[0] += 1   
    id_pedido = str(contador_id_pedidos[0]) 
    if cuit_cliente not in pedidos_clientes:
        pedidos_clientes[cuit_cliente] = {}
    pedidos_clientes[cuit_cliente][id_pedido] = platos_pedido

    print(pedidos_clientes)


def baja_plato(platos: dict, contador_id_platos: list[str]) -> None:
    for plato in platos:
        print(plato, ": ", platos(plato))
    id_a_eliminar: str = input("Elija que plato desea borrar: ")
    if id_a_eliminar in platos:
        platos.pop(id_a_eliminar)
    else:
        print("El dato ingresado no existe")

def modificar_plato(platos: dict, contador_id_platos: list[str]) -> None:
    for plato in platos:
        print(plato, ": ", platos(plato))
    id_a_modificar: str = input("Elija el plato a modificar: ")
    nuevo_nombre: str = input("Elija el nuevo nombre: ")
    nuevo_precio: int = float(input("Elija el nuevo precio: "))
    platos[id_a_modificar] = {"nombre": nuevo_nombre, "precio": nuevo_precio }
    


def alta_platos(platos: dict, contador_id_platos: list[str]) -> None:
    seguir_ingresando = "Si"
    while seguir_ingresando == "Si":
        nombre = input("Nombre del plato: ")
        precio = float(input("Ingrese precio del plato: "))
        contador_id_platos[0] += 1
        id_plato = str(contador_id_platos[0])
        platos[id_plato] = {"nombre": nombre, "precio": precio }
        seguir_ingresando: str = (input("Desea seguir agregando platos? (Si/No)"))

def abm_platos(platos: dict, contador_id_platos: list[str]) -> None:
    continuar = "Si"
    while continuar == "Si":
        print("ABM de platos")
        print("1. Alta plato")
        print("2. Modificar plato")
        print("3. Baja plato")
        print()
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            alta_platos(platos, contador_id_platos)
        elif opcion == 2:
            modificar_plato(platos)
        elif opcion == 3:
            baja_plato(platos)
        continuar: str = input("Desea continuar con el ABM? (Si/No): ")

def mostrar_menu(menu: list[str]) -> None:
    for item in menu:
        print(f"{item}: {menu[item]}")
    print()


def main() -> None:
    menu: dict[str] = {
       "a": "ABM de platos",
       "b": "Agregar un pedido",
       "c": "Listar pedidos por CUIT",
       "d": "Mostrar pedido con mayor valor",
       "e": "Mostrar el cliente con más pedidos",
       "f": "Mostrar el plato más solicitado",
       "g": "Salir"   
    }


    # platos = { id_pedido: { "nombre": , "precio":  } }
    # platos = { "1": { "nombre": "milanesa", "precio": 6500 } }
    platos: dict = {} 
    
    #pedidos_clientes = { cuit_cliente: { id_pedido: [plato1, plato2, .. ]} }
    pedidos_clientes = {}

    contador_id_platos: list[int] = [0]
    contador_id_pedidos: list[int] = [0]

    continuar = "Si"
    while continuar == "Si":
        mostrar_menu(menu)
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "a":
            abm_platos(platos, contador_id_platos)
        elif opcion == "b":
            agregar_pedido(platos, pedidos_clientes, contador_id_pedidos)
        elif opcion == "c":
            listar_pedidos(pedidos_clientes, platos)
        elif opcion == "d":
            mostrar_pedido_mayor_valor(pedidos_clientes)
        elif opcion == "e":
            mostrar_el_cliente_mas_pedidos(pedidos_clientes)
        elif opcion == "f":
            mostrar_plato_mas_solicitado(platos)
        
        continuar = input("Desea continuar? (Si/No): ")
main()
