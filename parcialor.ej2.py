def datos_parrafo(parrafo:str) -> None:
    palabra_mas_corta: str = ""
    palabra_mas_larga: str = ""
    cantidad_letras_corta: int = 0
    cantidad_letras_larga: int = 0
    
    parrafo_sin_coma = parrafo.replace(",", "")
    parrafo_definitivo = parrafo_sin_coma.split(" ")
    
    for i in range(len(parrafo_definitivo))
        parrafo_definitivo[i] = (parrafo_definitivo[i]).upper
    
    apariciones = {}
    for palabra in parrafo_definitivo:
        if palabra in apariciones:
            apariciones[palabra] += 1
        else:
            apariciones[palabra] = 1
    return apariciones
    

def main -> None:

    parrafo:str = “Las personas mayores nunca son capaces de comprender las cosas por sí mismas, y es muy
    aburrido para los niños tener que darles una y otra vez explicaciones.”
    
    datos_parrafo(parrafo)
    
main()

