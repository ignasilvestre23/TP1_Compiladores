from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 12: MANEJO DE ERRORES LÉXICOS
# ============================================================================
def ejercicio_12():
    """EJERCICIO 12: Manejo de errores léxicos"""
    casos = ["A = 10 @ B;", "precio = 25 # cantidad;", "usuario = $100;"]
 
    for cadena in casos:
        analizador = AnalizadorLexico()
        tokens = analizador.analizar(cadena)
 
        print(f"\nEntrada: {cadena}")
        print("Tokens:")
        for t in tokens:
            print(f"  {t.tipo:<20} {t.lexema}")
 
        if analizador.errores:
            print("Errores léxicos:")
            for e in analizador.errores:
                print(f"  carácter: {e.lexema!r}  línea: {e.linea}  columna: {e.columna}")
        else:
            print("Sin errores léxicos.")
if __name__ == "__main__":
    ejercicio_12()
