from os import system
from lexer import tokenisasi


def main():
    system('cls')
    while True:

        print('\n1. Input\n2. Generate case\n3. Exit')
        p = input('Pilih : ')
        system('cls')
        if p == '1':
            case = input('\nInput : ')
            tokens = tokenisasi(case.lower().strip())
            print('Output : {0}'.format(' '.join([str(token) for token in tokens])))
        elif p == '2':
            test_case = [
                'p and q or r',
                'if p then (not q s)',
                'p xor (q and not(p and q))',
                '(p and q ifg(r or s)'
            ]

            for case in test_case:
                tokens = tokenisasi(case.lower().strip())
                output = ' '.join([str(token) for token in tokens])
                print('\nInput : '+case)
                print('Output : {0}\n{1}'.format(output, '_'*(len(output)*2)))
        else:
            break


main()
