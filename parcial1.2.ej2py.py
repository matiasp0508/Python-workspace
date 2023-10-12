def stats_parrafo(parrafo: str) -> None:
    cantidad_palabras: int = 0
    palabra_mas_frecuente: str = ""
    porcentaje_vocales: float = 0
    palabra_mas_corta: str = ""
    palabra_mas_larga: str = ""


    palabras_parrafo = parrafo.split(" ")

    cantidad_palabras = len(palabras_parrafo)


    apariciones_palabra: dict[str, int] = {}  # { "texto": 2, "desde": 4 }
    for palabra in palabras_parrafo:
        if palabra not in apariciones_palabra:
            apariciones_palabra[palabra] = 1
        else:
            apariciones_palabra[palabra] += 1
    max_apariciones: int = 0
    primer_palabra: bool = True
    for palabra in apariciones_palabra:
        if primer_palabra:
            max_apariciones = apariciones_palabra[palabra]
            palabra_mas_frecuente = palabra
            primer_palabra = False
        if apariciones_palabra[palabra] > max_apariciones:
            max_apariciones = apariciones_palabra[palabra]
            palabra_mas_frecuente = palabra

    
    contador_vocales: int = 0
    vocales: list[str] = ["a", "e", "i", "o", "u"]
    for letra in parrafo:
        if letra.lower() in vocales:
            contador_vocales += 1
    porcentaje_vocales = round(contador_vocales / len(parrafo) * 100, 2)

    
    # palabra_mas_corta = ...
    # palabra_mas_larga = ...


    print("La cantidad de palabras que contiene el parrafo es: ", cantidad_palabras)
    print("La palabra mas frecuente del parrafo es: ", palabra_mas_frecuente)
    print("El porcentaje de vocales del parrafo es: ", porcentaje_vocales)
    print("La palabra mas larga del parrafo es: ", palabra_mas_larga)
    print("La palabra mas corta del parrafo es: ", palabra_mas_corta)


def main() -> None:
    parrafo: str = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto."

    stats_parrafo(parrafo)


main()