from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 7: ANALIZADOR DE EXPRESIONES
# ============================================================================
def ejercicio_7():
    """EJERCICIO 7: Analizador de expresiones"""
    cadena = "A = 10 + B;"
 
    analizador = AnalizadorLexico()
    tokens = analizador.analizar(cadena)
 
    print(f"Entrada: {cadena}")
    print(f"{'TOKEN':<25} {'LEXEMA'}")
    print("-" * 40)
    for t in tokens:
        tipo = t.tipo.replace("NUMERO_ENTERO", "NUMERO").replace("NUMERO_DECIMAL", "NUMERO")
        print(f"{tipo:<25} {t.lexema}")
if __name__ == "__main__":
    ejercicio_7()