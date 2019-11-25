def cipher(msg, r, logic):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    m = ''
    for caracter in msg:
        if caracter in alphabet:
            caracter_index = alphabet.index(caracter)
            if logic:
                m += alphabet[(caracter_index + r) % len(alphabet)]
            else:
                m += alphabet[(caracter_index - r) % len(alphabet)]
        else:
            m += caracter
    return m


def encrypt(msg, ro):
    return cipher(msg, ro, True)


def decrypt(msg, ro):
    return cipher(msg, ro, False)

