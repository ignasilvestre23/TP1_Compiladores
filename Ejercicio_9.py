from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 9: ANÁLISIS DE CADENAS
# ============================================================================
def ejercicio_9():
    """EJERCICIO 9: Análisis de cadenas"""
    cadena = 'nombre = "Juan";'
 
    analizador = AnalizadorLexico()
    tokens = analizador.analizar(cadena)
 
    print(f"Entrada: {cadena}")
    print(f"{'TOKEN':<20} {'LEXEMA'}")
    print("-" * 40)
    for t in tokens:
        print(f"{t.tipo:<20} {t.lexema}")

if __name__ == "__main__":
    ejercicio_9()  
    