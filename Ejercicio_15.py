import os
from Analizador_lexico import AnalizadorLexico
RUTA_ARCHIVO = "programa.txt"
 
CONTENIDO_EJEMPLO = (
    "int contador = 10;\n"
    "float precio = 25.50;\n"
    "contador = contador + 1;\n"
    "@\n"
)

# ============================================================================
# EJERCICIO 15: ANALIZAR UN ARCHIVO
# ============================================================================
def ejercicio_15():
    """EJERCICIO 15: Analizar un archivo"""
    if not os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            f.write(CONTENIDO_EJEMPLO)
        print(f"(No existía '{RUTA_ARCHIVO}', se creó uno de ejemplo)")
 
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        codigo = f.read()
 
    analizador = AnalizadorLexico()
    analizador.analizar(codigo)
 
    print(f"Contenido de '{RUTA_ARCHIVO}':\n{codigo}")
    print(analizador.generar_tabla())
    print(analizador.generar_tabla_errores())

if __name__ == "__main__":
    ejercicio_15()
