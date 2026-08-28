#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EJERCICIO 3: PALABRAS RESERVADAS - TP1 COMPILADORES
Reconocimiento de palabras reservadas vs identificadores
"""
 
import re
 
 
class PalabrasReservadas:
    """Reconocimiento de palabras reservadas"""
    
    PALABRAS = {
        'if', 'then', 'else', 'while', 'for', 'def', 'return',
        'int', 'float', 'string', 'bool', 'do', 'switch', 'case',
        'default', 'break', 'continue', 'char', 'double', 'void'
    }
    
    @staticmethod
    def es_palabra_reservada(texto: str) -> bool:
        """Verifica si el texto es exactamente una palabra reservada"""
        return texto.lower() in PalabrasReservadas.PALABRAS
    
    @staticmethod
    def es_identificador(texto: str) -> bool:
        """Verifica si es un identificador válido"""
        return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', texto))
 
 
def ejercicio_3():
    """EJERCICIO 3: Palabras reservadas"""
    print("\n" + "=" * 80)
    print("EJERCICIO 3: RECONOCIMIENTO DE PALABRAS RESERVADAS")
    print("=" * 80)
    
    print("\nPalabras reservadas disponibles:")
    palabras_ordenadas = sorted(PalabrasReservadas.PALABRAS)
    for i, palabra in enumerate(palabras_ordenadas, 1):
        print(f"  {palabra:15}", end=" " if i % 4 != 0 else "\n")
    print()
    
    print("\n" + "=" * 80)
    print("DIFERENCIACIÓN: PALABRA_RESERVADA vs IDENTIFICADOR")
    print("=" * 80)
    
    ejemplos_diferenciacion = [
        ("if", "PALABRA_RESERVADA (exacta)"),
        ("if123", "IDENTIFICADOR (contiene 'if' pero tiene más caracteres)"),
        ("int", "PALABRA_RESERVADA (exacta)"),
        ("inti", "IDENTIFICADOR (contiene 'int' pero tiene más caracteres)"),
    ]
    
    print("\nEjemplos de diferenciación:")
    for palabra, tipo_esperado in ejemplos_diferenciacion:
        es_reservada = PalabrasReservadas.es_palabra_reservada(palabra)
        es_ident = PalabrasReservadas.es_identificador(palabra)
        
        if es_reservada:
            clasificacion = "✓ PALABRA_RESERVADA"
        elif es_ident:
            clasificacion = "✓ IDENTIFICADOR"
        else:
            clasificacion = "✗ INVÁLIDO"
        
        print(f"  '{palabra:15}' → {clasificacion:30} | {tipo_esperado}")
    
    print("\n🧪 PRUEBA INTERACTIVA:")
    while True:
        entrada = input("\nIngresá una palabra (o 'salir'): ").strip()
        
        if entrada.lower() == 'salir':
            break
        
        if not entrada:
            print("⚠️  Entrada vacía")
            continue
        
        es_reservada = PalabrasReservadas.es_palabra_reservada(entrada)
        es_identificador = PalabrasReservadas.es_identificador(entrada)
        
        print(f"\n  '{entrada}':")
        if es_reservada:
            print(f"  ✓ Es una PALABRA_RESERVADA")
        elif es_identificador:
            print(f"  ✓ Es un IDENTIFICADOR válido")
        else:
            print(f"  ✗ No es válido (ni palabra reservada ni identificador)")
 
 
if __name__ == "__main__":
    ejercicio_3()
