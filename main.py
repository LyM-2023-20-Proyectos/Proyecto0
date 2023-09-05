import lexer
import P0_parser
import sys

prueba = "ValidProgram.txt"

def main():
    
    while True:
        text = input('Texto del programa> ')
        result, error = lexer.run('<current terminal input>', text)
        #parser = P0_parser.verificar_programa(text)

        if error:
            print(error.as_string())
            print('Programa inválido por caractér ilegal')
        else:
            print(result)
            print('Programa válido para el robot:',P0_parser.parse_line(result))
            #if parser:
            #    print('Programa valido')
            #if P0_parser.parse_line(result) == False:
            #    sys.exit()


if __name__ == '__main__':
    main()