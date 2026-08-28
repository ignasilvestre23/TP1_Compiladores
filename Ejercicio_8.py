from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 8: EXPRESIONES RELACIONALES
# ============================================================================
def ejercicio_8():
    """EJERCICIO 8: Expresiones relacionales"""
    casos = [
        "edad > 18;",
        "edad >= 18;",
        "edad < 18;",
        "edad <= 18;",
        "edad == 18;",
        "edad != 18;",
    ]
 
    for cadena in casos:
        analizador = AnalizadorLexico()
        tokens = analizador.analizar(cadena)
        print(f"\nEntrada: {cadena}")
        print(f"{'TOKEN':<25} {'LEXEMA'}")
        print("-" * 40)
        for t in tokens:
            tipo = t.tipo.replace("NUMERO_ENTERO", "NUMERO").replace("NUMERO_DECIMAL", "NUMERO")
            print(f"{tipo:<25} {t.lexema}")
if __name__ == "__main__":
    ejercicio_8()
