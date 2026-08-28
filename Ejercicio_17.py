from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 17: CASO INTEGRAL
# ============================================================================
def ejercicio_17():
    codigo = (
        "int edad = 25;\n"
        "float altura = 1.83;\n"
        "\n"
        "if edad >= 18 {\n"
        "    edad = edad + 1;\n"
        "}\n"
        "// Fin del programa\n"
    )
 
    analizador = AnalizadorLexico()
    tokens = analizador.analizar(codigo)
 
    print(f"Código fuente:\n{codigo}")
    print(analizador.generar_tabla())
    print(analizador.generar_tabla_errores())
    print(f"Cantidad total de tokens reconocidos: {len(tokens)}")
    print("\nNota: '// Fin del programa' fue reconocido como COMENTARIO y")
    print("descartado de la secuencia final de tokens (sin análisis sintáctico)."); """EJERCICIO 17: Caso de prueba integral"""


if __name__ == "__main__":
    ejercicio_17()
    