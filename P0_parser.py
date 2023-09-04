# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:59:58 2023

@author: Lucas Nieto Martínez
@author: 

Lexer
Módulo de análisis gramatical del proyecto 0 del curso ISIS-1106: Lenguaje y Máquinas
Parser True si un programa es válido, de lo contrario retorna false.
"""
import ProyecTokens as proTk
import lexer as lex
import builtins

#----------------------------------------------------
# Parser
#----------------------------------------------------

def parse_line(tokens):
    # Tokens es la lista de tokens retornada por el lexer
    current_token = 0
    valid_program = True

    while current_token in range(len(tokens)):
        # Una variable o procedimiento sólo puede tener de nombre un string
        if ((tokens[current_token] == proTk.T_defVar) or (tokens[current_token] == proTk.T_defProc)) and (proTk.T_str not in tokens[current_token+1]):
            valid_program = False
            break

        # Una variable con nombre sólo puede almacenar un número
        # Si un token es una definición de variable, el siguiente es token string, y el siguiente es token int
        if ((tokens[current_token] == proTk.T_defVar) and (proTk.T_str in tokens[current_token+1])):
            if (proTk.T_int not in tokens[current_token+2]):
                valid_program = False
                break

        # La definición de un procedimiento debe seguir la sintaxis:
        # defProc nomProc(...){
        #    ...
        # }
        # No sé arreglar esto
        if ((tokens[current_token] == proTk.T_defProc) and (proTk.T_str in tokens[current_token+1])):
            leftParenthesis = 0
            rightParenthesis = 0
            lBracket = 0
            rBracket = 0
            if (proTk.T_Lparent not in tokens[current_token+2]):
                print(proTk.T_Lparent)
                print(tokens[current_token+2])
                print(proTk.T_Lparent not in tokens[current_token+2])
                print(proTk.T_Lparent,'not in',tokens[current_token+2])
                valid_program = False
                break
            else:
                leftParenthesis += 1
                while current_token in range(len(tokens)):
                    if current_token == proTk.T_Lparent:
                        leftParenthesis += 1
                    elif current_token == proTk.T_Rparent:
                        rightParenthesis += 1
                        # Después del primer paréntesis derecho, debe venir un bracket izquierdo:
                        if (tokens[current_token] == proTk.T_Rparent) and (tokens[current_token+1] != proTk.T_Lbracket):
                            valid_program = False
                            break
                        else:
                            lBracket += 1
                            while current_token in range(len(tokens)):
                                if current_token == proTk.T_Lbracket:
                                    lBracket += 1
                                elif current_token == proTk.T_Rbracket:
                                    rBracket += 1
                                if lBracket != rBracket:
                                    valid_program = False
                                    break
                    current_token += 1
                if leftParenthesis != rightParenthesis:
                    valid_program = False
                    break
            


        
        current_token += 1

    return valid_program


#----------------------------------------------------
#Verificacion Funciones
#----------------------------------------------------

"""
def verificar_programa(txt)-> bool:
    tokens = lex.Lexer.makeTokens(txt)
    componentes = bloques_de_funciones(tokens)

    if componentes is None:
        return False
    else: 
        verificacion = verificar_componentes(componentes)
    return verificacion

def verificar_componentes(componentes):
    valido = True
    i = 0
    while i < len(componentes) and valido:
        func_actual = componentes[i]
        if func_actual[0] is (proTk.T_defVar):
            # No puede ser numero, defVar, defProd o {. Python tiene la funcion isnumeric() para verificar si un str es solamente numeros pero no se me importa
            if (func_actual[1].isnumeric()) or (func_actual[1] is (proTk.T_defVar or proTk.T_defProc or proTk.T_Lbracket)):
                valido = False
            if not (func_actual[2].isnumeric()):
                valido = False
        elif func_actual[0] is (proTk.T_defProc):
            if (func_actual[1].isnumeric()) or (func_actual[1] is (proTk.T_defVar or proTk.T_defProc or proTk.T_Lbracket)):
                valido = False

            tupla_valido_i = revisar_parametros(func_actual)
            valido = tupla_valido_i[0]
            index = tupla_valido_i[1]
    
            if not valido:
                return False
            else:
                return True
        #elif func_actual[0] is (proTk.T_Lbracket):

        return valido


def bloques_de_funciones(tokens):
    #Cada funcion se define cuando comienza por defVar, defProc o {
    componentes = []
    valido = True
    i = 0

    while i < len(tokens) and valido:
        
        if tokens[i] is (proTk.T_defVar or proTk.T_defProc or proTk.T_Lbracket):
            
            if tokens[i] == proTk.T_defVar:

                bloque_i = bloque_defVar(i,tokens)
            else:
                bloque_i = bloque_defProc(i,tokens)
            
            var_o_func = bloque_i[0]
            i = bloque_i[1]
            componentes.append(var_o_func)
        else:
            componentes = None
            valido = False
    
    return componentes
                

def bloque_defVar(tokens, i):
    variable = []
    #La variable tiene 3 elementos: defVar, nombre y valor
    for pos in range(i, i+3):
        variable.append(tokens[pos])
    return variable, i+3

def bloque_defProc(tokens, i):
    funcion = []
    #Cuenta corchetes dentro de funciones. Cuando subfunc_abrir = 0, se cierra la funcion principal.
    subfunc_cerrar = 0
    subfunc_abrir = 1
    i += 1
    valido = True

    while i < len(tokens) and valido:
        token_actual = tokens[i:i+1]

        if token_actual == ("if" or "while" or "else"):
            subfunc_cerrar += 1
            subfunc_abrir += 1
        
        if token_actual is (proTk.T_defVar or proTk.T_defProc):
            funcion = tokens[i:i+1]
            valido = False

        elif token_actual == "{":
            if subfunc_abrir == 0:
                funcion = tokens[i:i+1]
                valido = False
            else:
                subfunc_abrir -= 1
        
        elif token_actual == "}":
            if subfunc_cerrar == 0:
                funcion = tokens[i:i+1]
                valido = False
            else:
                subfunc_cerrar -= 1
        
        i +=1
    return funcion, i
        

def revisar_parametros(parametros)->tuple:
    pos_ini = 2
    pos_fin = 2
    valido = True
    sublista = []
    
    while pos_fin < len(parametros) and valido:
        
        token = parametros[pos_fin]
        if token == ")":
            sublista = parametros[pos_ini : pos_fin+1]
        pos_fin +=1
                
    if len(sublista) != 0:
        valido = estructura_de_parametro(sublista)
        return valido,pos_fin+1
    else:
        return False,None

def estructura_de_parametro(sublista:list)->bool:
    
    #Lista de tokens entre parentesis en una funion defProc    
    valido = True
    pos = 1
    
    if sublista[0] != "(" or sublista[-1] != proTk.T_comma:
        return False
    
    while pos < len(sublista)-1 and valido:
        token = sublista[pos]
        
        if (pos == len(sublista)-2) and not (token is (proTk.T_defVar or proTk.T_defProc or proTk.T_Lbracket) or token == proTk.T_comma):
            valido = False
        elif pos%2 == 1 and (not token is (proTk.T_defVar or proTk.T_defProc or proTk.T_Lbracket)):
            valido = False
        elif pos%2 == 0 and token != proTk.T_comma:
            valido = False 
        pos += 1
        
    return valido
"""