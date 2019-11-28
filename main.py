from tba import tokenisasi,validasi

def main():
    while True:
        string = input('\nInput : ').lower().strip()
        tokens = tokenisasi(string)
        print('Output (Token Lexic) : {0}'.format(' '.join([str(token) for token in tokens])))
        validasi(tokens)
main()

