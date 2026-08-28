from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 13: PRIORIDAD DE RECONOCIMIENTO
# ============================================================================
def ejercicio_13():
    """EJERCICIO 13: Prioridad de reconocimiento"""
    print("Explicación:")
    print(" - Los patrones se recorren en orden y se usa la PRIMERA coincidencia.")
    print(" - Los operadores compuestos (==, !=, <=, >=) están definidos antes")
    print("   que los operadores simples (=, <, >), así que '==' nunca se parte")
    print("   en dos tokens '=' '='.\n")
 
    casos = ["A = B;", "A == B;", "A > B;", "A >= B;",
             "A < B;", "A <= B;", "A != B;"]
 
    for cadena in casos:
        analizador = AnalizadorLexico()
        tokens = analizador.analizar(cadena)
        print(f"Entrada: {cadena}")
        for t in tokens:
            tipo = t.tipo.replace("NUMERO_ENTERO", "NUMERO").replace("NUMERO_DECIMAL", "NUMERO")
            print(f"  {tipo:<25} {t.lexema}")
        print()
        
if __name__ == "__main__":
    ejercicio_13()
