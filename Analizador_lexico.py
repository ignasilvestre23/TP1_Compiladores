#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLASES COMPARTIDAS - TP1 COMPILADORES
Definiciones de datos y utilidades comunes para todos los ejercicios
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
import re


# ============================================================================
# ENUMERACIONES Y ESTRUCTURAS DE DATOS
# ============================================================================

class TipoToken(Enum):
    """Tipos de tokens reconocibles en el analizador léxico"""
    TIPO_DATO = "TIPO_DATO"
    PALABRA_RESERVADA = "PALABRA_RESERVADA"
    IDENTIFICADOR = "IDENTIFICADOR"
    NUMERO_ENTERO = "NUMERO_ENTERO"
    NUMERO_DECIMAL = "NUMERO_DECIMAL"
    CADENA = "CADENA"
    OPERADOR_ARITMETICO = "OPERADOR_ARITMETICO"
    OPERADOR_RELACIONAL = "OPERADOR_RELACIONAL"
    OPERADOR_LOGICO = "OPERADOR_LOGICO"
    ASIGNACION = "ASIGNACION"
    DELIMITADOR = "DELIMITADOR"
    COMENTARIO = "COMENTARIO"
    DESCONOCIDO = "DESCONOCIDO"


@dataclass
class Token:
    """Representación de un token"""
    tipo: str
    lexema: str
    linea: int = 1
    columna: int = 1
    
    def __repr__(self):
        return f"Token({self.tipo}, {self.lexema!r}, {self.linea}, {self.columna})"


@dataclass
class ErrorLexico:
    """Representación de un error léxico"""
    lexema: str
    linea: int
    columna: int
    descripcion: str = "Token desconocido"
    
    def __repr__(self):
        return f"Error({self.lexema!r} L{self.linea}C{self.columna}: {self.descripcion})"


# ============================================================================
# ANALIZADOR LÉXICO PRINCIPAL
# ============================================================================

class AnalizadorLexico:
    """
    Analizador léxico completo para el TP1 de Compiladores.
    Reconoce tipos de datos, palabras reservadas, identificadores,
    números, cadenas, operadores y delimitadores.
    """
    
    def __init__(self):
        self.tokens = []
        self.errores = []
        self._inicializar_patrones()
    
    def _inicializar_patrones(self):
        """Inicializa los patrones regex para cada tipo de token"""
        self.patrones = [
            # Comentarios (deben procesarse antes que operadores)
            (r'//[^\n]*', TipoToken.COMENTARIO.value),
            (r'/\*.*?\*/', TipoToken.COMENTARIO.value),
            
            # Cadenas de caracteres
            (r'"[^"]*"', TipoToken.CADENA.value),
            (r"'[^']*'", TipoToken.CADENA.value),
            
            # Números (decimales antes que enteros)
            (r'[+-]?\d+\.\d+', TipoToken.NUMERO_DECIMAL.value),
            (r'[+-]?\d+', TipoToken.NUMERO_ENTERO.value),
            
            # Operadores compuestos (antes que operadores simples)
            (r'==', TipoToken.OPERADOR_RELACIONAL.value),
            (r'!=', TipoToken.OPERADOR_RELACIONAL.value),
            (r'<=', TipoToken.OPERADOR_RELACIONAL.value),
            (r'>=', TipoToken.OPERADOR_RELACIONAL.value),
            (r'&&', TipoToken.OPERADOR_LOGICO.value),
            (r'\|\|', TipoToken.OPERADOR_LOGICO.value),
            
            # Operadores simples
            (r'[+\-*/%]', TipoToken.OPERADOR_ARITMETICO.value),
            (r'[<>]', TipoToken.OPERADOR_RELACIONAL.value),
            (r'!', TipoToken.OPERADOR_LOGICO.value),
            (r'=', TipoToken.ASIGNACION.value),
            
            # Tipos de datos
            (r'\b(int|float|string|bool|char|double|void)\b', TipoToken.TIPO_DATO.value),
            
            # Palabras reservadas
            (r'\b(if|then|else|while|for|do|def|return|switch|case|default|break|continue)\b', TipoToken.PALABRA_RESERVADA.value),
            
            # Identificadores
            (r'[a-zA-Z_][a-zA-Z0-9_]*', TipoToken.IDENTIFICADOR.value),
            
            # Delimitadores
            (r'[{}()\[\];,.]', TipoToken.DELIMITADOR.value),
        ]
    
    def analizar(self, codigo: str) -> List[Token]:
        """Analiza el código y retorna lista de tokens"""
        self.tokens = []
        self.errores = []
        
        linea = 1
        columna = 1
        pos = 0
        
        while pos < len(codigo):
            # Saltar espacios en blanco pero actualizar línea y columna
            if codigo[pos] == '\n':
                linea += 1
                columna = 1
                pos += 1
                continue
            elif codigo[pos] in ' \t\r':
                columna += 1
                pos += 1
                continue
            
            # Intentar coincidencia con cada patrón
            coincidencia = None
            for patron, tipo_token in self.patrones:
                regex = re.compile(patron, re.DOTALL)
                match = regex.match(codigo, pos)
                if match:
                    lexema = match.group(0)
                    token = Token(tipo_token, lexema, linea, columna)
                    
                    # No agregar comentarios a la lista de tokens
                    if tipo_token != TipoToken.COMENTARIO.value:
                        self.tokens.append(token)
                    
                    # Actualizar posición y columna
                    pos = match.end()
                    if '\n' in lexema:
                        linea += lexema.count('\n')
                        columna = len(lexema.split('\n')[-1]) + 1
                    else:
                        columna += len(lexema)
                    
                    coincidencia = True
                    break
            
            # Si no hay coincidencia, registrar error
            if not coincidencia:
                lexema = codigo[pos]
                error = ErrorLexico(lexema, linea, columna, "Token desconocido")
                self.errores.append(error)
                pos += 1
                columna += 1
        
        return self.tokens
    
    def generar_tabla(self) -> str:
        """Genera una tabla formateada de tokens"""
        if not self.tokens:
            return "No hay tokens para mostrar\n"
        
        output = "\n" + "=" * 80 + "\n"
        output += "TABLA DE TOKENS\n"
        output += "=" * 80 + "\n"
        output += f"{'#':<4} {'TIPO':<30} {'LEXEMA':<20} {'LÍN':<4} {'COL':<4}\n"
        output += "-" * 80 + "\n"
        
        for i, token in enumerate(self.tokens, 1):
            output += f"{i:<4} {token.tipo:<30} {token.lexema!r:<20} {token.linea:<4} {token.columna:<4}\n"
        
        output += "=" * 80 + "\n"
        return output
    
    def generar_tabla_errores(self) -> str:
        """Genera una tabla de errores léxicos"""
        if not self.errores:
            return "Sin errores léxicos\n"
        
        output = "\n" + "=" * 80 + "\n"
        output += "TABLA DE ERRORES LÉXICOS\n"
        output += "=" * 80 + "\n"
        output += f"{'#':<4} {'LEXEMA':<20} {'LÍN':<4} {'COL':<4} {'DESCRIPCIÓN':<40}\n"
        output += "-" * 80 + "\n"
        
        for i, error in enumerate(self.errores, 1):
            output += f"{i:<4} {error.lexema!r:<20} {error.linea:<4} {error.columna:<4} {error.descripcion:<40}\n"
        
        output += "=" * 80 + "\n"
        return output
    
    def generar_estadisticas(self) -> str:
        """Genera estadísticas del análisis"""
        total_tokens = len(self.tokens)
        total_errores = len(self.errores)
        
        # Contar por tipo
        conteo_tipos = {}
        for token in self.tokens:
            conteo_tipos[token.tipo] = conteo_tipos.get(token.tipo, 0) + 1
        
        output = "\n" + "=" * 80 + "\n"
        output += "ESTADÍSTICAS DEL ANÁLISIS\n"
        output += "=" * 80 + "\n"
        output += f"Total de tokens reconocidos: {total_tokens}\n"
        output += f"Total de errores léxicos: {total_errores}\n"
        output += "\nDistribución de tokens por tipo:\n"
        
        for tipo, cantidad in sorted(conteo_tipos.items()):
            porcentaje = (cantidad / total_tokens * 100) if total_tokens > 0 else 0
            output += f"  {tipo:<30}: {cantidad:>4} ({porcentaje:>5.1f}%)\n"
        
        output += "=" * 80 + "\n"
        return output
