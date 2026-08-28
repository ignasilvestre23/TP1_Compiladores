#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MENÚ PRINCIPAL - TP1 COMPILADORES
Analizador Léxico - Análisis Léxico, Expresiones Regulares y Tokens
"""

import sys
import os

# Importar ejercicios
from Ejercicio_2 import ejercicio_2
from Ejercicio_3 import ejercicio_3
from Ejercicio_4 import ejercicio_4
from Ejercicio_5 import ejercicio_5
from Ejercicio_6 import ejercicio_6
from Ejercicio_7 import ejercicio_7
from Ejercicio_8 import ejercicio_8
from Ejercicio_9 import ejercicio_9
from Ejercicio_10 import ejercicio_10
from Ejercicio_11 import ejercicio_11
from Ejercicio_12 import ejercicio_12
from Ejercicio_13 import ejercicio_13
from Ejercicio_14 import ejercicio_14
from Ejercicio_15 import ejercicio_15
from Ejercicio_16 import ejercicio_16
from Ejercicio_17 import ejercicio_17
from Ejercicio_18 import ejercicio_18
from Ejercicio_19 import ejercicio_19

def menu_principal():
    """Menú principal que permite elegir qué ejercicio ejecutar"""
    ejercicios = {
        '2': ('Expresiones regulares', ejercicio_2),
        '3': ('Palabras reservadas', ejercicio_3),
        '4': ('Reconocimiento de operadores', ejercicio_4),
        '5': ('Reconocimiento de delimitadores', ejercicio_5),
        '6': ('Primer analizador léxico', ejercicio_6),
        '7': ('Analizador de expresiones', ejercicio_7),
        '8': ('Expresiones relacionales', ejercicio_8),
        '9': ('Análisis de cadenas', ejercicio_9),
        '10': ('Análisis de comentarios', ejercicio_10),
        '11': ('Manejo de espacios', ejercicio_11),
        '12': ('Manejo de errores léxicos', ejercicio_12),
        '13': ('Prioridad de reconocimiento', ejercicio_13),
        '14': ('Línea y columna', ejercicio_14),
        '15': ('Analizar un archivo', ejercicio_15),
        '16': ('Generación de tabla de tokens', ejercicio_16),
        '17': ('Caso de prueba integral', ejercicio_17),
        '18': ('Casos inválidos', ejercicio_18),
        '19': ('Pruebas del analizador', ejercicio_19),
    }
 
    while True:
        print("\n" + "=" * 50)
        print("     TP1 COMPILADORES - ANÁLISIS LÉXICO")
        print("=" * 50)
 
        for numero in sorted(ejercicios.keys(), key=int):
            nombre, _ = ejercicios[numero]
            print(f"  {numero:>2}) {nombre}")
 
        print("   s) Salir")
        print("=" * 50)
 
        opcion = input("\nElegí un ejercicio: ").strip().lower()
 
        if opcion == 's' :
            print("\n¡Hasta luego!")
            break
 
        entrada_menu = ejercicios.get(opcion)
        if entrada_menu:
            _, funcion = entrada_menu
            try:
                funcion()
            except KeyboardInterrupt:
                print("\n\nOperación cancelada")
            except Exception as e:
                print(f"\n❌ Error al ejecutar ejercicio: {e}")
        else:
            print("\n⚠️  Opción inválida")


if __name__ == "__main__":
    menu_principal()