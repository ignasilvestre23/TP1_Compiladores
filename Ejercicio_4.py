"""
EJERCICIOS 4-19 - TP1 COMPILADORES
Todos los ejercicios intermedios en un módulo
"""
 
import re
from Analizador_lexico import AnalizadorLexico
 
 
# ============================================================================
# EJERCICIO 4: OPERADORES
# ============================================================================
def ejercicio_4():
    """EJERCICIO 4: Reconocimiento de operadores"""
    print("\n" + "=" * 80)
    print("EJERCICIO 4: RECONOCIMIENTO DE OPERADORES")
    print("=" * 80)
    
    operadores = {
        'Aritméticos': ['+', '-', '*', '/', '%'],
        'Relacionales': ['<', '>', '<=', '>=', '==', '!='],
        'Lógicos': ['&&', '||', '!'],
        'Asignación': ['=', '+=', '-=', '*=', '/='],
    }
    
    for categoria, ops in operadores.items():
        print(f"\n{categoria}:")
        print(f"  {', '.join(ops)}")
    
    analizador = AnalizadorLexico()
    print("\n🧪 PRUEBA: Análisis de expresión con operadores")
    
    expresiones = [
        "a + b",
        "x > 5",
        "true && false",
        "contador += 1",
        "a == b"
    ]
    
    for expr in expresiones:
        print(f"\n  {expr}")
        tokens = analizador.analizar(expr)
        ops = [t for t in tokens if 'OPERADOR' in t.tipo or t.tipo == 'ASIGNACION']
        if ops:
            print(f"  → Operadores: {[op.lexema for op in ops]}")

if __name__ == "__main__":
    ejercicio_4()