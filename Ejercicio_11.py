from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 11: MANEJO DE ESPACIOS
# ============================================================================
def ejercicio_11():
    """EJERCICIO 11: Manejo de espacios"""
    variantes = [
    "A=10+B;",
    "A = 10 + B;",
    "A    =    10   +   B;",
]
 
    secuencias = []
    for cadena in variantes:
        analizador = AnalizadorLexico()
        tokens = analizador.analizar(cadena)
        secuencia = [(t.tipo, t.lexema) for t in tokens]
        secuencias.append(secuencia)
 
        print(f"\nEntrada: {cadena!r}")
        for t in tokens:
            print(f"  {t.tipo:<25} {t.lexema}")
 
    todas_iguales = all(s == secuencias[0] for s in secuencias)
    print(f"\n¿Las tres variantes producen la misma secuencia de tokens? "
          f"{'SÍ' if todas_iguales else 'NO'}")

if __name__ == "__main__":
    ejercicio_11()