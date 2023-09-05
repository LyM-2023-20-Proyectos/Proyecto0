import lexer
import P0_parser
import sys

archivo = "ValidProgram.txt"

with open(archivo, 'r') as texto:
    programa = texto.read()

def main():
    
    while True:
        result, error = lexer.run(f'File: {archivo}', programa)
        parser = P0_parser.parse(programa)

        if error:
            print(error.as_string())
            print('Programa inválido por caractér ilegal')
            sys.exit()
        else:
            print(result)
            print('Programa válido para el robot:',P0_parser.parse_line(result))
            if parser:
                print('Programa valido?')
            if P0_parser.parse(result) == False:
                print(False)
                print(sys.exit())