from lexer import Lexer


def main():

    string = input('Input : ')

    tokens = Lexer(string.lower()).tokenisasi()

    print('Output : {0}'.format(' '.join([str(token) for token in tokens])))


main()
