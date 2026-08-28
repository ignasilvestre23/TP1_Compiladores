from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 14: LÍNEA Y COLUMNA
# ============================================================================
def ejercicio_14():
    """EJERCICIO 14: Información de línea y columna"""
    codigo = (
        "int contador = 10;\n"
        "float precio = 25.50;\n"
        "edad = edad + 1;\n"
    )
 
    analizador = AnalizadorLexico()
    tokens = analizador.analizar(codigo)
 
    print(f"Entrada:\n{codigo}")
    print(f"{'LINEA':<6} {'COLUMNA':<8} {'TOKEN':<25} {'LEXEMA'}")
    print("-" * 60)
    for t in tokens:
        tipo = t.tipo.replace("NUMERO_ENTERO", "NUMERO").replace("NUMERO_DECIMAL", "NUMERO")
        print(f"{t.linea:<6} {t.columna:<8} {tipo:<25} {t.lexema}")

if __name__ == "__main__":
    ejercicio_14()
