#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EJERCICIO 2: EXPRESIONES REGULARES - TP1 COMPILADORES
Análisis de patrones para identificadores, números y cadenas
"""
 
import re
 
 
# ============================================================================
# EJERCICIO 2a: IDENTIFICADOR
# ============================================================================
class RegexIdentificador:
    """
    Identificador: Debe comenzar con una letra y posteriormente
    podrá contener: letras, números, guión bajo
    """
    PATRON = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    EJEMPLOS_VALIDOS = [
        "nombre",
        "contador",
        "contador1",
        "usuario_1",
        "_variable"
    ]
    
    EJEMPLOS_INVALIDOS = [
        "123nombre",      # No comienza con letra
        "1usuario",       # No comienza con letra
        "usuario-",       # Contiene guión
        "@nombre"         # Contiene carácter especial
    ]
    
    EXPLICACION = """
    Expresión Regular: ^[a-zA-Z_][a-zA-Z0-9_]*$
    - ^: Inicio de cadena
    - [a-zA-Z_]: Primer carácter debe ser letra (mayúscula/minúscula) o guión bajo
    - [a-zA-Z0-9_]*: Seguido de cero o más letras, números o guiones bajos
    - $: Fin de cadena
    """
    
    @staticmethod
    def validar(texto: str) -> bool:
        return bool(re.match(RegexIdentificador.PATRON, texto))
 
 
# ============================================================================
# EJERCICIO 2b: NÚMERO ENTERO
# ============================================================================
class RegexNumeroEntero:
    """
    Número entero: Reconocer números enteros con signo opcional
    """
    PATRON = r'^[+-]?\d+$'
    
    EJEMPLOS_VALIDOS = [
        "10",
        "125",
        "999",
        "-15",
        "+20"
    ]
    
    EJEMPLOS_INVALIDOS = [
        "10.5",           # Tiene decimal
        "abc",            # No es número
        "12a",            # Contiene letra
        "- 15"            # Espacio en el medio
    ]
    
    EXPLICACION = """
    Expresión Regular: ^[+-]?\\d+$
    - ^: Inicio de cadena
    - [+-]?: Signo opcional (+ o -)
    - \\d+: Uno o más dígitos
    - $: Fin de cadena
    """
    
    @staticmethod
    def validar(texto: str) -> bool:
        return bool(re.match(RegexNumeroEntero.PATRON, texto))
 
 
# ============================================================================
# EJERCICIO 2c: NÚMERO DECIMAL
# ============================================================================
class RegexNumeroDecimal:
    """
    Número decimal: Reconocer números decimales con signo opcional
    """
    PATRON = r'^[+-]?\d+\.\d+$'
    
    EJEMPLOS_VALIDOS = [
        "10.5",
        "3.14",
        "25.00",
        "-15.75",
        "+3.14"
    ]
    
    EJEMPLOS_INVALIDOS = [
        "10",             # No tiene decimal
        "10.",            # Falta parte decimal
        ".5",             # Falta parte entera
        "12.5.8",         # Múltiples puntos
        "abc",            # No es número
        "1a.5"            # Contiene letra
    ]
    
    EXPLICACION = """
    Expresión Regular: ^[+-]?\\d+\\.\\d+$
    - ^: Inicio de cadena
    - [+-]?: Signo opcional
    - \\d+: Dígitos para parte entera
    - \\.: Punto literal
    - \\d+: Dígitos para parte decimal
    - $: Fin de cadena
    """
    
    @staticmethod
    def validar(texto: str) -> bool:
        return bool(re.match(RegexNumeroDecimal.PATRON, texto))
 
 
# ============================================================================
# EJERCICIO 2d: CADENA DE CARACTERES
# ============================================================================
class RegexCadenaCaracteres:
    """
    Cadena de caracteres: Reconocer cadenas encerradas entre comillas dobles
    """
    PATRON = r'^"[^"]*"$'
    
    EJEMPLOS_VALIDOS = [
        '"Hola"',
        '"Juan"',
        '"Compiladores"',
        '"Hola mundo"',
        '""'              # Cadena vacía
    ]
    
    EJEMPLOS_INVALIDOS = [
        'Hola',           # Sin comillas
        '"Hola',          # Comilla faltante
        'Hola"',          # Comilla faltante
        '"Hola\'',        # Comillas diferentes
        "'Hola'"          # Comillas simples
    ]
    
    EXPLICACION = """
    Expresión Regular: ^"[^"]*"$
    - ^: Inicio de cadena
    - ": Comilla doble de apertura
    - [^"]*: Cero o más caracteres que no sean comilla doble
    - ": Comilla doble de cierre
    - $: Fin de cadena
    """
    
    @staticmethod
    def validar(texto: str) -> bool:
        return bool(re.match(RegexCadenaCaracteres.PATRON, texto))
 
 
# ============================================================================
# FUNCIÓN DEL EJERCICIO 2
# ============================================================================
 
def ejercicio_2():
    """
    Ejercicio 2 del documento:
    Expresiones regulares para: identificador, número entero,
    número decimal y cadena de caracteres.
    """
    print("\n" + "=" * 80)
    print("EJERCICIO 2: EXPRESIONES REGULARES")
    print("=" * 80)
 
    subejercicios = {
        'a': ('Identificador', RegexIdentificador),
        'b': ('Número entero', RegexNumeroEntero),
        'c': ('Número decimal', RegexNumeroDecimal),
        'd': ('Cadena de caracteres', RegexCadenaCaracteres),
    }
 
    while True:
        print("\nSubejercicios disponibles:")
        for letra, (nombre, _) in subejercicios.items():
            print(f"  {letra}) {nombre}")
        print("  q) Volver al menú principal")
 
        opcion = input("\nElegí un subejercicio: ").strip().lower()
 
        if opcion == 'q':
            break
 
        if opcion not in subejercicios:
            print("\n⚠️  Opción inválida")
            continue
 
        nombre, clase = subejercicios[opcion]
 
        print(f"\n--- {nombre} ---")
        print(clase.EXPLICACION)
 
        print("Ejemplos válidos:")
        for ej in clase.EJEMPLOS_VALIDOS:
            resultado = "✓ VÁLIDO" if clase.validar(ej) else "✗ INVÁLIDO"
            print(f"  {ej!r:20} → {resultado}")
 
        print("\nEjemplos inválidos:")
        for ej in clase.EJEMPLOS_INVALIDOS:
            resultado = "✓ VÁLIDO" if clase.validar(ej) else "✗ INVÁLIDO"
            print(f"  {ej!r:20} → {resultado}")
 
        print("\n🧪 PRUEBA INTERACTIVA:")
        while True:
            entrada = input(f"\nIngresá un texto para validar como {nombre.lower()} (o 'volver'): ")
            if entrada.lower() == 'volver':
                break
 
            resultado = "✓ VÁLIDO" if clase.validar(entrada) else "✗ INVÁLIDO"
            print(f"  {entrada!r} → {resultado}")
 
 
if __name__ == "__main__":
    ejercicio_2()