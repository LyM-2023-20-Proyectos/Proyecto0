import lexer
import P0_parser

def main():
    
    while True:
        text = input('Texto del programa> ')
        result, error = lexer.run('<current terminal input>', text)

        if error:
            print(error.as_string())
            print('Programa inválido por caractér ilegal')
        else:
            print(result,'Programa válido para el robot:',P0_parser.parse_line(result))


if __name__ == '__main__':
    main()