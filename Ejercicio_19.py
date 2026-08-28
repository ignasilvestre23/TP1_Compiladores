import os
from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 19: Pruebas del analizador
# ============================================================================

MENU = (
    "\n========================================\n"
    "           ANALIZADOR LEXICO\n"
    "========================================\n"
    "1. Ingresar cadena\n"
    "2. Analizar archivo\n"
    "3. Mostrar tokens\n"
    "4. Mostrar errores\n"
    "5. Mostrar estadísticas\n"
    "6. Salir\n"
)

def ejercicio_19():
    """EJERCICIO 19: Pruebas del analizador"""
    analizador = AnalizadorLexico()
 
    while True:
        print(MENU)
        opcion = input("Seleccione una opción: ").strip()
 
        if opcion == "1":
            entrada = input("Ingrese la cadena a analizar: ")
            analizador.analizar(entrada)
            print(f"\nTokens reconocidos: {len(analizador.tokens)}")
            print(f"Errores léxicos: {len(analizador.errores)}")
 
        elif opcion == "2":
            ruta = input("Ruta del archivo a analizar: ").strip()
            if not os.path.exists(ruta):
                print(f"El archivo '{ruta}' no existe.")
                continue
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            analizador.analizar(contenido)
            lineas = contenido.count("\n") + (1 if contenido and not contenido.endswith("\n") else 0)
            print("\n========================================")
            print("        RESULTADO DEL ANALISIS")
            print("========================================")
            print(f"Tokens reconocidos: {len(analizador.tokens)}")
            print(f"Errores léxicos: {len(analizador.errores)}")
            print(f"Líneas analizadas: {lineas}")
            print("========================================")
 
        elif opcion == "3":
            print(analizador.generar_tabla())
 
        elif opcion == "4":
            print(analizador.generar_tabla_errores())
 
        elif opcion == "5":
            print(analizador.generar_estadisticas())
 
        elif opcion == "6":
            print("Saliendo del analizador léxico.")
            break
 
        else:
            print("Opción inválida, intente nuevamente.")
if __name__ == "__main__":
    ejercicio_19()