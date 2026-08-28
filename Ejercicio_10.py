from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 10: ANÁLISIS DE COMENTARIOS
# ============================================================================
def ejercicio_10():
    """EJERCICIO 10: Análisis de comentarios"""
    casos = ["// comentario", "// Hola mundo", "edad = 18; // edad"]
 
    for cadena in casos:
        analizador = AnalizadorLexico()
        tokens = analizador.analizar(cadena)
        print(f"\nEntrada: {cadena}")
        print(f"{'TOKEN':<20} {'LEXEMA'}")
        print("-" * 40)
        if not tokens:
            print("(el comentario fue reconocido y descartado de la secuencia final)")
        for t in tokens:
            print(f"{t.tipo:<20} {t.lexema}")
if __name__ == "__main__":
    ejercicio_10()
