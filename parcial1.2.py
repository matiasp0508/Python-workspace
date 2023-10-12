def mostrar_plato_mas_solicitado(platos: dict, pedidos_clientes: dict) -> None:
    pass


def mostrar_cliente_con_mas_pedidos(pedidos_clientes: dict, platos: dict) -> None:
    cliente_mas_pedidos = 0
    for max_pedidos in pedidos_clientes.values():
        if len(max_pedidos[1]) > cliente_mas_pedidos:
            cliente_mas_pedidos = len(max_pedidos[1])
            cuit_cliente = max_pedidos[0]
            total_pedidos = max_pedidos[1]
    
    total = 0
    for id_plato in platos:
        for id_plato in platos[id_plato]:pass

    # pedidos_clientes = { cuit_cliente: { id_pedido: [plato1, plato2...] } }
    # pedidos_clientes = {
    #     "123456789": {
    #         "pedido1": ["plato1", "plato2", "plato3"]
    #     },
    #     "376437345": {
    #         "pedido2": ["plato2", "plato4"]
    #     },
    # }

    # platos = { id_plato: { nombre, valor }}
    # platos = { "plato1": { "nombre": "milanesa", "valor": 6500.00 } }

def mostrar_pedido_con_mayor_valor(pedidos_clientes: dict, platos: dict) -> None:
    maximo_valor: int = 0
    id_pedido_maximo_valor: str = ""
    primer_id: bool = True
    for cuit_cliente in pedidos_clientes:
        for id_pedido in pedidos_clientes[cuit_cliente]:
            valor_total_pedido: int = 0
            for id_plato in pedidos_clientes[cuit_cliente][id_pedido]:
                valor_plato = platos[id_plato]["valor"]
                valor_total_pedido += valor_plato
            if primer_id:
                maximo_valor = valor_total_pedido
                id_pedido_maximo_valor = id_pedido
                primer_id = False
            if valor_total_pedido > maximo_valor:
                maximo_valor = valor_total_pedido
                id_pedido_maximo_valor = id_pedido
    print("El id de pedido con el mayor valor es: ", id_pedido_maximo_valor)
    print("Su valor total es: ", maximo_valor)
            

def listar_pedidos_por_cuit(pedidos_clientes: dict) -> None:
    cuit_cliente = input("Ingrese el cuit para ver sus pedidos: ")
    for pedido in pedidos_clientes[cuit_cliente]:
        print(pedido, ": ", pedidos_clientes[cuit_cliente][pedido])


def pedido_valido(string: str, platos: dict) -> bool:
    split = string.split(",")
    # El formato es válido
    for s in split:
        if not s.isnumeric():
            return False
    # Hay al menos 1 plato
    if len(split) < 1:
        return False
    # Existe el plato
    for id_ in split:
        if id_ not in platos:
            return False
    return True


def agregar_pedido(platos: dict, pedidos_clientes: dict, contador_id_pedidos: list[int]) -> None:
    for plato in platos:
        print(plato, ": ", platos[plato])
    cuit_cliente: str = input("Ingrese el cuit del cliente: ")
    ingreso_pedido: str = input("Ingrese los platos del pedido, separados por coma (ej: 1,2,3)")
    if not pedido_valido(ingreso_pedido, platos):
        while not pedido_valido(ingreso_pedido, platos):
            platos_pedido: str = input("Ingrese los platos del pedido, separados por coma (ej: 1,2,3)")
    platos_pedido: list[str] = ingreso_pedido.split(",")
    contador_id_pedidos[0] += 1
    id_pedido = str(contador_id_pedidos[0])
    if cuit_cliente not in pedidos_clientes:
        pedidos_clientes[cuit_cliente] = {}
    pedidos_clientes[cuit_cliente][id_pedido] = platos_pedido


def alta_plato(platos: dict, contador_id_platos: list[int]) -> None:
    seguir_ingresando: str = "Si"

    while seguir_ingresando == "Si":
        nombre = input("Nombre del plato: ")
        valor = float(input("Valor del plato: "))
        contador_id_platos[0] += 1
        id_plato = str(contador_id_platos[0])
        platos[id_plato] = { "nombre": nombre, "valor": valor }

        seguir_ingresando: str = input("Seguir ingresando platos? (Si/No)")


def modificar_plato(platos: dict) -> None:
    for plato in platos:
        print(plato, ": ", platos[plato])
    id_a_modificar: str = input("Elija el plato que desea modificar: ")
    nuevo_nombre: str = input("Ingrese el nuevo nombre del plato: ")
    nuevo_valor: str = input("Ingrese el nuevo valor del plato: ")
    platos[id_a_modificar] = { "nombre": nuevo_nombre, "valor": nuevo_valor }


def baja_plato(platos: dict) -> None:
    for plato in platos:
        print(plato, ": ", platos[plato])
    id_a_borrar: str = input("Elija el plato que desea borrar: ")
    if id_a_borrar in platos:
        platos.pop(id_a_borrar)


def abm_platos(platos: dict, contador_id_platos: list[int]) -> None:
    continuar = "Si"
    while continuar == "Si":
        print("ABM de platos")
        print("1) Alta plato")
        print("2) Baja plato")
        print("3) Modificacion plato")
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            alta_plato(platos, contador_id_platos)
        elif opcion == 2:
            baja_plato(platos)
        elif opcion == 3:
            modificar_plato(platos)
        continuar: str = input("Seguir con ABM de platos? (Si/No)")


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
    }

    # pedidos_clientes = { cuit_cliente: { id_pedido: [plato1, plato2...] } }
    # pedidos_clientes = {
    #     "123456789": {
    #         "pedido1": ["plato1", "plato2", "plato3"]
    #     },
    #     "376437345": {
    #         "pedido2": ["plato2", "plato4"]
    #     },
    # }
    pedidos_clientes: dict = {}

    # platos = { id_pedido: { nombre, valor }}
    # platos = { "plato1": { "nombre": "milanesa", "valor": 6500.00 } }
    platos: dict = {}  

    contador_id_platos: list[int] = [0]
    contador_id_pedidos: list[int] = [0]

    continuar: bool = "Si"
    while continuar == "Si":
        mostrar_menu(menu)
        opcion: str = input("Ingrese la opcion que desea: ")
        if opcion == "a":
            abm_platos(platos, contador_id_platos)  ## check
        elif opcion == "b":
            agregar_pedido(platos, pedidos_clientes, contador_id_pedidos)  ## check
        elif opcion == "c":
            listar_pedidos_por_cuit(pedidos_clientes)  ## check
        elif opcion == "d":
            mostrar_pedido_con_mayor_valor(pedidos_clientes, platos)
        elif opcion == "e":
            mostrar_cliente_con_mas_pedidos(pedidos_clientes)
        elif opcion == "f":
            mostrar_plato_mas_solicitado(platos, pedidos_clientes)
        continuar: str = input("Continuar? (Si/No)")


main()