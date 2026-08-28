import re
from Analizador_lexico import AnalizadorLexico

# ============================================================================
# EJERCICIO 5: DELIMITADORES
# ============================================================================
def ejercicio_5():
    """EJERCICIO 5: Reconocimiento de delimitadores"""
    print("\n" + "=" * 80)
    print("EJERCICIO 5: RECONOCIMIENTO DE DELIMITADORES")
    print("=" * 80)
    
    delimitadores = {
        'Llaves': ['{', '}'],
        'Paréntesis': ['(', ')'],
        'Corchetes': ['[', ']'],
        'Puntuación': [';', ',', '.'],
    }
    
    print("\nDelimitadores reconocidos:")
    for categoria, delim in delimitadores.items():
        print(f"  {categoria}: {' '.join(delim)}")
    
    analizador = AnalizadorLexico()
    print("\n🧪 PRUEBA: Análisis de estructura con delimitadores")
    
    codigo = "int arr[10]; for(i=0; i<10; i++) { arr[i] = i; }"
    print(f"\n  Código: {codigo}")
    tokens = analizador.analizar(codigo)
    delims = [t for t in tokens if t.tipo == 'DELIMITADOR']
    print(f"  → Delimitadores: {[d.lexema for d in delims]}")

if __name__ == "__main__":
    ejercicio_5()