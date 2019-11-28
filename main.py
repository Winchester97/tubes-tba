from tba import tokenisasi,validasi


def main():
    while True:
        # [1, 5, 9, 1, 3, 2, 9, 1, 3, 1, 10, 10]
        string = input('\nInput : ').lower().strip()
        tokens = tokenisasi(string)
        print('Output (Token Lexic) : {0}'.format(' '.join([str(token) for token in tokens])))
        if validasi(tokens):
            print('Valid')
        else:
            print('Tidak valid')


main()

