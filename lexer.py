def tokenisasi(string):

    state_pqrs = lambda string : state_error() if (bool(string)) else 1
    state_n = lambda string : state_no(string[1:]) if (bool(string) and string[0]=='o') else state_error()
    state_no = lambda string : state_not(string[1:]) if (bool(string) and string[0]=='t') else state_error()
    state_not = lambda string : state_error() if (bool(string)) else 2
    state_a = lambda string : state_an(string[1:]) if (bool(string) and string[0]=='n') else state_error()
    state_an = lambda string : state_and(string[1:]) if (bool(string) and string[0]=='d') else state_error()
    state_and = lambda string : state_error() if (bool(string)) else 3
    state_o = lambda string : state_or(string[1:]) if (bool(string) and string[0]=='r') else state_error()
    state_or = lambda string : state_error() if (bool(string)) else 4
    state_x = lambda string : state_xo(string[1:]) if (bool(string) and string[0]=='o') else state_error()
    state_xo = lambda string : state_xor(string[1:]) if (bool(string) and string[0]=='r') else state_error()
    state_xor = lambda string : state_error() if (bool(string)) else 5
    state_i = lambda string : state_if(string[1:]) if (bool(string) and string[0]=='f') else state_error()
    state_if = lambda string : cek_iff(string) if (bool(string)) else 6
    cek_iff = lambda string : state_iff(string[1:]) if (bool(string) and string[0]=='f') else state_error()
    state_iff = lambda string : state_error() if (bool(string)) else 8
    state_t = lambda string : state_th(string[1:]) if (bool(string) and string[0]=='h') else state_error()
    state_th = lambda string : state_the(string[1:]) if (bool(string) and string[0]=='e') else state_error()
    state_the = lambda string : state_then(string[1:]) if (bool(string) and string[0]=='n') else state_error()
    state_then = lambda string : state_error() if (bool(string)) else 7
    state_bukakurung = lambda : 9
    state_tutupkurung = lambda : 10
    state_error = lambda : 'error'

    def state_initial(string):
        proposisi = ['p','q','r','s']
        char = string[0]
        if (char in proposisi): return state_pqrs(string[1:])
        elif (char == 'n'): return state_n(string[1:])
        elif (char == 'a'): return state_a(string[1:])
        elif (char == 'o'): return state_o(string[1:])
        elif (char == 'x'): return state_x(string[1:])
        elif (char == 'i'): return state_i(string[1:])
        elif (char == 't'): return state_t(string[1:])
        elif (char == '('): return state_bukakurung()
        elif (char == ')'): return state_tutupkurung()
        else: return state_error()

    tokens = []
    word = ''

    def input_token(w):
        if bool(w):
            token = state_initial(w)
            tokens.append(token)
            if token == 'error': return False
            nonlocal word
            word = ''

    for i, char in enumerate(string):
        if char != ' ':
            if (char == '('):
                if (bool(word) and (input_token(word) is False)): break
                if (input_token(char) is False): break
            elif char == ')':
                if (bool(word) and (input_token(word) is False)): break
                if (input_token(char) is False): break
            else:
                word += char
        else:
            if (input_token(word) is False): break

    try:
        if tokens[-1] != 'error':
            input_token(word)
    except IndexError:
        input_token(word)

    return tokens
