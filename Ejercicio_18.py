from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 18: CASOS INVÁLIDOS
# ============================================================================
def ejercicio_18():
    """EJERCICIO 18: Pruebas con casos inválidos"""
    casos = ["123abc", "@usuario", '"Hola', "12.5.8", "A === B", "#contador"]
 
    for cadena in casos:
        analizador = AnalizadorLexico()
        tokens = analizador.analizar(cadena)
 
        print(f"\nEntrada: {cadena}")
        print(f"  Tokens reconocidos: {[(t.tipo, t.lexema) for t in tokens]}")
 
        if analizador.errores:
            print("  Tipo de error: ERROR LEXICO")
            for e in analizador.errores:
                print(f"  Lexema/carácter problemático: {e.lexema!r}")
                print(f"  Línea: {e.linea}  Columna: {e.columna}")
                print(f"  Acción: informar error y continuar el análisis")
        else:
            print("  Tipo de error: ninguno detectado por el analizador léxico")
            print("  (los caracteres son válidos, se descomponen en varios")
            print("   tokens en lugar de un único error; ver docstring)")
if __name__ == "__main__":
    ejercicio_18()
