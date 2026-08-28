from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 16: TABLA DE TOKENS
# ============================================================================
def ejercicio_16():
    """EJERCICIO 16: Generación de tabla de tokens"""
    codigo = (
        "int contador = 10;\n"
        "float precio = 25.50;\n"
        "contador = contador + 1;\n"
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
    ejercicio_16()
