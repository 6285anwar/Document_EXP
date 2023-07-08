
def function_in_file1(s):
    main = s+'anwar'
    return main


def create_mapping():
    # Define your custom mapping here
    mapping = {
        'A':'HJ7$',
        'B':'rf$H',
        'C':'j][c',
        'D':'B47-',
        'E':'8jh#',
        'F':'7VH!',
        'G':'#YU@',
        'H':'^KZ%',
        'I':'QWAS',
        'J':'MNBV',
        'K':'XJLN',
        'L':'CTUI',
        'M':'PLOK',
        'N':'GHJK',
        'O':'TSRQ',
        'P':'DHGF',
        'Q':'ZXCV',
        'R':'EDCB',
        'S':'AEFR',
        'T':'GYKL',
        'U':'IMJV',
        'V':'CPFZ',
        'W':'d323',
        'X':'23rf',
        'Y':'ewd3',
        'Z':'wed2',

        'a': 'Kl*(',
        'b': 'gh%3',
        'c': '57da',
        'd': 'sS5!',
        'e': '^j7!',
        'f': '@L8#',
        'g': '$k9%',
        'h': '&p4*',
        'i': '(u6)',
        'j': ')y2.',
        'k': '-q1,',
        'l': '=w0?',
        'm': 'qwf3',
        'n': 'rht5',
        'o': '!ez7',
        'p': '#fhD',
        'q': 'gHj7',
        'r': 'ads2',
        's': "jkly",
        't': '3qed',
        'u': 'efwd',
        'v': ',bnm',
        'w': '.zyx',
        'x': '24df',
        'y': 'Tg&4',
        'z': '3fss',
        '1': '/;@3',
        '2': '"#rf',
        '3': "'$fQ",
        '4': 'Hgj3',
        '5':'mnru',
        '6': '%op8',
        '7': '&*ys',
        '8': '(^zx',
        '9': ')!cv',
    
    }
    return mapping

def encrypt(plaintext, mapping):
    encrypted_text = ""
    for char in plaintext:
        if char in mapping:
            encrypted_text += mapping[char]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, mapping):
    reversed_mapping = {v: k for k, v in mapping.items()}
    decrypted_text = ""
    i = 0
    while i < len(encrypted_text):
        found = False
        for length in range(len(max(mapping.values(), key=len)), 0, -1):
            if encrypted_text[i:i+length] in reversed_mapping:
                decrypted_text += reversed_mapping[encrypted_text[i:i+length]]
                i += length
                found = True
                break
        if not found:
            decrypted_text += encrypted_text[i]
            i += 1
    return decrypted_text

def encript(text):
    custom_mapping = create_mapping()
    encrypted_message = encrypt(text, custom_mapping)
    return(encrypted_message)

def decript(result1):
    custom_mapping = create_mapping()
    decrypted_message = decrypt(result1, custom_mapping)
    return(decrypted_message)
