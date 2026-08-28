from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 6: PRIMER ANALIZADOR LÉXICO
# ============================================================================
def ejercicio_6():
    """EJERCICIO 6: Primer analizador léxico"""
    cadena = input("Ingrese una cadena a analizar (Enter = usar ejemplo 'A = 10;'): ").strip()
    if not cadena:
        cadena = "A = 10;"
 
    analizador = AnalizadorLexico()
    tokens = analizador.analizar(cadena)
 
    print(f"\nEntrada: {cadena}")
    print(f"{'TOKEN':<20} {'LEXEMA'}")
    print("-" * 40)
    for t in tokens:
        # NUMERO_ENTERO / NUMERO_DECIMAL se muestran como "NUMERO" según el enunciado
        tipo = t.tipo.replace("NUMERO_ENTERO", "NUMERO").replace("NUMERO_DECIMAL", "NUMERO")
        print(f"{tipo:<20} {t.lexema}")
if __name__ == "__main__":
    ejercicio_6()