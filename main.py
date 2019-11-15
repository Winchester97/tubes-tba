from lexer import tokenisasi


def main():

    string = input('Input : ')
    tokens = tokenisasi(string.lower().strip())
    print('Output : {0}'.format(' '.join([str(token) for token in tokens])))

main()
